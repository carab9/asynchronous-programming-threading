from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

class FileIO:
    def __init__(self):
        pass

    @staticmethod
    def _open_html_site(html_site):
        html = urlopen(html_site)
        return BeautifulSoup(html, 'html.parser')

    @staticmethod
    def scrape_page(website):
        soup = FileIO._open_html_site(website)
        found = None
        for table in soup.find_all('table'):
            print(table.attrs)
            if table.get('class') == ['table', 'table-bordered', 'table-condensed', 'table-striped', 'table-header']:
                found = table
                break
        table = found

        table_head = table.find('thead')
        if table_head:
            rows = table_head.find_all('tr')
            for row in rows:
                cols = row.find_all('th')
                cols = [ele.text.strip() for ele in cols]
                if cols:
                    col_names = cols

        df = pd.DataFrame(columns=col_names)

        try:
            table_body = table.find('tbody')
            if table_body:
                rows = table_body.find_all('tr')
                for row in rows:
                    # Get headers

                    cols = row.find_all('td')
                    cols = [x.text.strip() for x in cols]
                    if cols:
                        df.loc[len(df.index)] = cols
        except ValueError as exc:
            print("Error:", str(exc))
            raise RuntimeError from exc
        finally:
            print("Ending")
            return df