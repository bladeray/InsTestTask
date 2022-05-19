from locust import HttpUser, task, between


class N11User(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_base_page(self):
        base_page = self.client.get("/")
        assert 'n11.com - Hayat Sana Gelir' in base_page.text

    @task
    def get_search_request(self):
        self.client.get("/arama?q=phone")
        self.client.get("/arama?q=new+balance")
        self.client.get("/arama?q=casio")
        self.client.get("/arama?q=ikea")
        self.client.get("/arama?q=pet")
        self.client.get("/arama?q=Oculus+Quest+2+Sanal+Ger%C3%A7eklik+G%C3%B6zl%C3%BC%C4%9F%C3%BC")
        self.client.get("/telefon-ve-aksesuarlari/cep-telefonu?q=iphone+11&md=Iphone+11-Iphone+11+Pro-Iphone+11+Pro+Max")

    @task
    def get_products_from_results(self):
        self.client.get("/urun/apple-iphone-11-64-gb-apple-turkiye-garantili-1109951?magaza=teknonet")
        self.client.get("/urun/apple-iphone-13-128-gb-apple-turkiye-garantili-2141312?magaza=bittibitiyor")
        self.client.get("/gunluk-spor-ayakkabi/new-balance-ms009bnr-erkek-gunluk-ayakkabi-ms009bnr-gri-P522269141")
        self.client.get("/gunluk-spor-ayakkabi/new-balance-erkek-ayakkabi-m990nv5-P453038823")
        self.client.get("/urun/casio-edifice-ef-539d-1avdf-erkek-kol-saati-967759?magaza=gundogdusaat")
        self.client.get("/urun/casio-efr-s107l-1avudf-edifice-erkek-kol-saati-2193565?magaza=watchcenter")
        self.client.get("/urun/ikea-nyskoljd-thetasarim-bulasik-kurutma-ortusu-koyu-gri-4801044?magaza=thetasarim")
        self.client.get("/urun/bulasik-kabi-17x14x8-cm-saklama-kutusu-bulasiklik-gri-ikea-4802235?magaza=qualityshopp")
        self.client.get("/urun/brt-pet-kedi-yatagi-60-x-45-x-17-cm-2541471?magaza=dukkanseninn")
        self.client.get("/urun/brt-pet-simit-seklinde-polar-kedi-yatagi-50-x-12-cm-2109429?magaza=dukkanseninn")
        self.client.get("/urun/oculus-quest-2-all-in-one-kablosuz-vr-sanal-gerceklik-gozlugu-128-gb-2103463?magaza=flytechnology")
        self.client.get("/urun/oculus-quest-2-all-in-one-kablosuz-vr-sanal-gerceklik-gozlugu-256-gb-1576813?magaza=flytechnology")
        self.client.get("/urun/apple-iphone-11-128-gb-apple-turkiye-garantili-1107897?magaza=cephaneteknoloji")
        self.client.get("/urun/apple-iphone-11-128-gb-apple-turkiye-garantili-1107897?magaza=akyol-iletisim")
