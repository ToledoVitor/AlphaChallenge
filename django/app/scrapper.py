import pandas as pd
import requests
from bs4 import BeautifulSoup
from django.core.exceptions import ValidationError
from requests.models import Response

from app.models import Cotacao


class ScrapperClient:
    url = 'https://valorinveste.globo.com/cotacoes/'
    table_ids = {
        'Cotacões Intradia': 'cotacoes-intradia',
        'BDRs mais negociados': 'bdrs-mais-negociados',
        'Fundos Imobiliários': 'fundos-imobiliarios',
    }
    table_headers = {
        'Nome': 'name',
        'Código': 'code',
        'Última (R$)': 'last_price',
        'Variação (%)': 'last_day_price',
        'Fech. dia anterior (R$)': 'variation',
    }

    def __init__(self, url=None) -> None:
        if url:
            self.url = url

    def scrap(self) -> None:
        page = self._get_request()
        soup = BeautifulSoup(page.text, 'lxml')
        for table_id in self.table_ids.values():
            dataframe = self._create_dataframe(soup, table_id)
            self._save_dataframe_in_database(dataframe, table_id)

    def _get_request(self) -> Response:
        page = requests.get(self.url)
        if page.status_code != 200:
            raise ValidationError(
                f'The request returned a {page.status_code} status'
            )

        return page

    def _get_table_data(self, table):
        # Going through the second element removes the table headers
        return table.find_all('tr')[1:]

    def _create_dataframe(
        self, soup: BeautifulSoup, table_id: str
    ) -> pd.DataFrame:
        table = soup.find('div', id=table_id)
        if not table:
            raise ValidationError(
                f'BeatifulSoup cant find a div with id {table_id}'
            )

        table = table.find('tbody')
        table_data = self._get_table_data(table)

        df = pd.DataFrame(columns=self.table_headers.values())
        df = self._populate_dataframe(df, table_data)
        return df

    def _populate_dataframe(self, df, data):
        for tr in data:
            row_data = tr.find_all('td')
            row = [dt.text.strip() for dt in row_data]

            length = len(df)
            df.loc[length] = row

        return df

    def _save_dataframe_in_database(
        self, df: pd.DataFrame, table_id: str
    ) -> None:
        df_records = df.to_dict('records')
        cotacoes = [
            self._cotacoes_from_record(record=record, table_id=table_id)
            for record in df_records
        ]
        Cotacao.objects.bulk_create(cotacoes)

    def _cotacoes_from_record(self, record: dict, table_id: str):
        try:
            last_price = float(record['last_price'].replace(',', '.'))
            last_day_price = float(
                record['last_day_price'].replace(',', '.').replace(' %', '')
            )
            variation = float(record['variation'].replace(',', '.'))
        except (ValueError, TypeError):
            last_price = None
            last_day_price = None
            variation = None

        return Cotacao(
            table=table_id,
            name=record['name'],
            code=record['code'],
            last_price=last_price,
            last_day_price=last_day_price,
            variation=variation,
        )
