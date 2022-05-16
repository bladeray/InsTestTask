from locust import HttpUser, task, between


class N11User(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_products_for_each_category(self):
        self.client.get("/kadin-ceket/mavi-jill-90-s-gri-jean-ceket-110081-32651-P446745171")
        self.client.get("/urun/wechip-h96-mini-h8-2g16g-16-gb-android-tv-box-1761089?magaza=meldeticaret")
        self.client.get("/koltuk-takimi/hazal-oturma-gurubu-3311-mavi-lacivert-P524851582")
        self.client.get("/urun/dr-browns-options-pp-biberon-dar-agiz-120-ml-2888972?magaza=pharmastore")
        self.client.get("/urun/braun-exactfit-1-bua-5000-ust-koldan-olcer-tansiyon-aleti-siyah-1752958?magaza=hometicaret")
        self.client.get("/urun/casio-edifice-ef-539d-1avdf-erkek-kol-saati-967759?magaza=gundogdusaat")
        self.client.get("/urun/hypervolt-bluetooth-masaj-aleti-4303353?magaza=ardsport")
        self.client.get("/promosyon/kirtasiye-eksiklerini-firsatlarla-tamamla-1440364")
        self.client.get("/urun/continental-20555r16-91v-premiumcontact-6-2022-2447608?magaza=simetrilastik")

    @task
    def get_categories(self):
        self.client.get("/giyim-ayakkabi")
        self.client.get("/elektronik")
        self.client.get("/ev-yasam")
        self.client.get("/anne-bebek")
        self.client.get("/kozmetik-kisisel-bakim")
        self.client.get("/mucevher-saat")
        self.client.get("/spor-outdoor")
        self.client.get("/kitap-muzik-film-oyun")
        self.client.get("/otomotiv-motosiklet")
