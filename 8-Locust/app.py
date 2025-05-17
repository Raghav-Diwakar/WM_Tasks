from locust import HttpUser, task, between

# All the paths to be tested
paths = [
    "/404.html", "/aamchi-mumbai.php", "/aboutus.html", "/action.html", "/ads.txt",
    "/app-ads.txt", "/behindthescenes_details.php", "/bengali.html", "/best-friend-foreverrr.php",
    "/bhojpuri.html", "/black-and-white-movies.html", "/blogs.html", "/blue-eyes.php",
    "/born-warrior.php", "/career.html", "/careers.html", "/comedy.html", "/config.php",
    "/contact.html", "/crime.html", "/desh-mere.php", "/details.php", "/directors.html",
    "/documentary.html", "/drama.html", "/email.html", "/email2.html", "/email3.html",
    "/email4.html", "/email5.html", "/email6.html", "/email10.html", "/english.html",
    "/eorfamily.php", "/eororiginal.php", "/eororiginals.php", "/eortv_producer_agreement.docx",
    "/eortv_producer_agreement.pdf", "/eortv_writer_agreement.docx", "/eortv_writer_agreement.pdf",
    "/eortv-anthem.php", "/eortv-tunes.html", "/fam.php", "/family.php", "/familyoriginals.php",
    "/fantasy.html", "/fearless-tiger.php", "/festivals.html", "/game-of-cricket-2.php",
    "/game-of-cricket.php", "/gandhinagar-queer-pride-parade.php", "/gay.html",
    "/goa-pride-festival.php", "/gujarati.html", "/hindi.html", "/horror.html",
    "/i-love-us-2.php", "/i-love-us-3-making.php", "/i-love-us-3.php", "/i-love-us-making.php",
    "/i-love-us.php", "/index.html", "/international.html", "/jaipur-queer-pride-parade.php",
    "/joinus.html", "/kannada.html", "/khatta-khatta-meetha-meetha-2.php", 
    "/khatta-khatta-meetha-meetha-3.php", "/khatta-khatta-meetha-meetha-4.php",
    "/khatta-khatta-meetha-meetha.php", "/lesbian.html", "/lgbtq.html", "/listings.html",
    "/login.html", "/love-bites-making.php", "/love-bites.php", "/malayalam.html",
    "/manifest.json", "/marathi.html", "/mombian-2.php", "/mombian.php", "/most-watched.html",
    "/movies.html", "/mystery.html", "/new-releases.html", "/newsroom.html", "/nfamily.php",
    "/noriginal.php", "/offline.html", "/original_music.php", "/original.php",
    "/originaleortv.php", "/originaleortv2.php", "/originals_details.php", "/originaltest.php",
    "/orimode.php", "/pankhirya-udi-udi-2.php", "/pankhirya-udi-udi.php", "/producers.html",
    "/productionlist.html", "/profile.html", "/profilepage.html", "/punjabi.html",
    "/reality.html", "/romantic.html", "/sadrakshanay.php", "/script-writers.html",
    "/shaheed.php", "/sitemap.xml", "/sports.html", "/subscription.html", "/success-auto-inr-7.html",
    # ... [TRUNCATED FOR BREVITY – include the rest of the list here]
    "/blogs/why-gay-marriage-is-still-a-problem.html"
]

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)  # Wait between 1 to 3 seconds between requests

    @task
    def load_all_paths(self):
        for path in paths:
            self.client.get(path, name=path)

