import requests
from bs4 import BeautifulSoup
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

with open("acoes.txt") as f:
    acoes = f.readlines()
acoes = [x.strip("\n") for x in acoes]

file = open("indicadoresAcoes.csv", "w", encoding="UTF-8")
file.write('"Empresa","Código","Segmento","Valor Atual","D.Y","P/L","P/VP","Peg Ratio","LPA","VPA","DivLiq/PL","DivLiq/Ebitda","Liq Corrente","ROE","ROIC","CAGR R","CAGR L","Mrg. Bruta","Mrg. Líquida","Mrg. Ebitda"\n')
file.close()

for line in acoes:
    codeAcao = line.strip().upper()
    try:
        print(codeAcao)
        if codeAcao.find("34") > 0:
            url = "https://statusinvest.com.br/bdrs/" + codeAcao
        else:
            url = "https://statusinvest.com.br/acoes/" + codeAcao
        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, "html.parser")
        dom = etree.HTML(str(soup))
        nomeAcao = dom.xpath('//*[@id="main-header"]/div[2]/div/div[1]/h1/small')[
            0
        ].text
        valorAtual = dom.xpath(
            '//*[@id="main-2"]/div[2]/div/div[1]/div/div[1]/div/div[1]/strong'
        )[0].text
        dy = dom.xpath(
            '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[1]/div/div/strong'
        )[0].text
        pl = dom.xpath(
            '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[2]/div/div/strong'
        )[0].text
        pvp = dom.xpath(
            '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[4]/div/div/strong'
        )[0].text
        pegRatio = dom.xpath(
            '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[3]/div/div/strong'
        )[0].text
        lpa = dom.xpath(
            '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[11]/div/div/strong'
        )[0].text
        vpa = dom.xpath(
            '//*[@id="indicators-section"]/div[2]/div/div[1]/div/div[9]/div/div/strong'
        )[0].text
        divPL = dom.xpath(
            '//*[@id="indicators-section"]/div[2]/div/div[2]/div/div[1]/div/div/strong'
        )[0].text
        divEbitda = dom.xpath(
            '//*[@id="indicators-section"]/div[2]/div/div[2]/div/div[2]/div/div/strong'
        )[0].text
        liqCorrente = dom.xpath(
            '//*[@id="indicators-section"]/div[2]/div/div[2]/div/div[6]/div/div/strong'
        )[0].text
        roe = dom.xpath(
            '//*[@id="indicators-section"]/div[2]/div/div[4]/div/div[1]/div/div/strong'
        )[0].text
        roic = dom.xpath(
            '//*[@id="indicators-section"]/div[2]/div/div[4]/div/div[3]/div/div/strong'
        )[0].text
        cagrR = dom.xpath(
            '//*[@id="indicators-section"]/div[2]/div/div[5]/div/div[1]/div/div/strong'
        )[0].text
        cagrL = dom.xpath(
            '//*[@id="indicators-section"]/div[2]/div/div[5]/div/div[2]/div/div/strong'
        )[0].text
        mBruta = dom.xpath(
            '//*[@id="indicators-section"]/div[2]/div/div[3]/div/div[4]/div/div/strong'
        )[0].text
        mLiq = dom.xpath(
            '//*[@id="indicators-section"]/div[2]/div/div[3]/div/div[4]/div/div/strong'
        )[0].text
        mEbitda = dom.xpath(
            '//*[@id="indicators-section"]/div[2]/div/div[3]/div/div[4]/div/div/strong'
        )[0].text
        try:
            segmento = dom.xpath(
                '//*[@id="company-section"]/div[1]/div/div[3]/div/div[3]/div/div/div/a/strong'
            )[0].text
        except:
            segmento = dom.xpath(
                '//*[@id="company-section"]/div[1]/div[3]/div/div[3]/div/div/div/a/strong'
            )[0].text

        with open("indicadoresAcoes.csv", "a", newline="", encoding="UTF-8") as r:
            linha = (
                '"'
                + nomeAcao
                + '","'
                + codeAcao
                + '","'
                + segmento
                + '","'
                + valorAtual
                + '","'
                + dy
                + '","'
                + pl
                + '","'
                + pvp
                + '","'
                + pegRatio
                + '","'
                + lpa
                + '","'
                + vpa
                + '","'
                + divPL
                + '","'
                + divEbitda
                + '","'
                + liqCorrente
                + '","'
                + roe
                + '","'
                + roic
                + '","'
                + cagrR
                + '","'
                + cagrL
                + '","'
                + mBruta
                + '","'
                + mLiq
                + '","'
                + mEbitda
                + '"'
                + "\n"
            )
            r.write(linha)
    except:
        print("Acao " + line + " nao encontrada!")

r.close()

