from locust import HttpUser, task, between
import random

class EORTVUser(HttpUser):
    wait_time = between(1, 5)

    # Main pages
    main_pages = [
        "/index.html",
        "/aboutus.html",
        "/contact.html",
        "/career.html",
        "/careers.html",
        "/joinus.html",
        "/subscription.html",
        "/login.html",
        "/profile.html",
        "/profilepage.html",
        "/newsroom.html",
        "/blogs.html",
        "/movies.html",
        "/web-series.html",
        "/most-watched.html",
        "/new-releases.html",
        "/top-trending.html",
        "/listings.html",
        "/directors.html",
        "/producers.html",
        "/script-writers.html",
        "/productionlist.html",
        "/sitemap.xml",
        "/manifest.json",
        "/offline.html",
        "/404.html",
        "/test.php",
        "/config.php",
        "/ads.txt",
        "/app-ads.txt"
    ]
    
    # Genre pages
    genres = [
        "/action.html",
        "/comedy.html",
        "/crime.html",
        "/documentary.html",
        "/drama.html",
        "/fantasy.html",
        "/horror.html",
        "/mystery.html",
        "/reality.html",
        "/romantic.html",
        "/sports.html",
        "/thrillers.html",
        "/tourism.html",
        "/black-and-white-movies.html",
        "/festivals.html",
        "/unseen-moments.html"
    ]
    
    # Language pages
    languages = [
        "/bengali.html",
        "/bhojpuri.html",
        "/english.html",
        "/gujarati.html",
        "/hindi.html",
        "/kannada.html",
        "/malayalam.html",
        "/marathi.html",
        "/punjabi.html",
        "/tamil.html",
        "/telugu.html",
        "/international.html"
    ]
    
    # LGBTQ+ category pages
    lgbtq_pages = [
        "/gay.html",
        "/lesbian.html",
        "/lgbtq.html",
        "/family.html",
        "/familyoriginals.php",
        "/fam.php",
        "/nfamily.php",
        "/noriginal.php",
        "/eorfamily.php",
        "/eororiginal.php",
        "/eororiginals.php",
        "/original.php",
        "/originaleortv.php",
        "/originaleortv2.php",
        "/originaltest.php",
        "/orimode.php",
        "/original_music.php",
        "/eortv-tunes.html",
        "/eortv-anthem.php"
    ]
    
    # Original content pages
    original_content = [
        "/aamchi-mumbai.php",
        "/best-friend-foreverrr.php",
        "/blue-eyes.php",
        "/born-warrior.php",
        "/desh-mere.php",
        "/details.php",
        "/behindthescenes_details.php",
        "/originals_details.php",
        "/fearless-tiger.php",
        "/game-of-cricket.php",
        "/game-of-cricket-2.php",
        "/gandhinagar-queer-pride-parade.php",
        "/goa-pride-festival.php",
        "/jaipur-queer-pride-parade.php",
        "/i-love-us.php",
        "/i-love-us-2.php",
        "/i-love-us-3.php",
        "/i-love-us-making.php",
        "/i-love-us-3-making.php",
        "/khatta-khatta-meetha-meetha.php",
        "/khatta-khatta-meetha-meetha-2.php",
        "/khatta-khatta-meetha-meetha-3.php",
        "/khatta-khatta-meetha-meetha-4.php",
        "/love-bites.php",
        "/love-bites-making.php",
        "/mombian.php",
        "/mombian-2.php",
        "/pankhirya-udi-udi.php",
        "/pankhirya-udi-udi-2.php",
        "/sadrakshanay.php",
        "/shaheed.php",
        "/the-last-flight.php",
        "/u-only-complete-me.php",
        "/we-too-are-equal.php",
        "/wrong-number.php"
    ]
    
    # Documents
    documents = [
        "/eortv_producer_agreement.docx",
        "/eortv_producer_agreement.pdf",
        "/eortv_writer_agreement.docx",
        "/eortv_writer_agreement.pdf",
        "/documents/complaint-form.html",
        "/documents/data_deletion.html",
        "/documents/disclaimer.html",
        "/documents/privacy-policy.html",
        "/documents/terms.html"
    ]
    
    # Email templates
    email_templates = [
        "/email.html",
        "/email2.html",
        "/email3.html",
        "/email4.html",
        "/email5.html",
        "/email6.html",
        "/email10.html"
    ]
    
    # Success pages
    success_pages = [
        "/success.html",
        "/success-couponcode.html",
        "/success-inr-7.html",
        "/success-inr-20.html",
        "/success-inr-30.html",
        "/success-inr-60.html",
        "/success-inr-90.html",
        "/success-inr-180.html",
        "/success-inr-365.html",
        "/success-usd-7.html",
        "/success-usd-20.html",
        "/success-usd-30.html",
        "/success-usd-60.html",
        "/success-usd-90.html",
        "/success-usd-180.html",
        "/success-usd-365.html",
        "/success-auto-inr-7.html",
        "/success-auto-inr-20.html",
        "/success-auto-inr-30.html",
        "/success-auto-inr-60.html",
        "/success-auto-inr-90.html",
        "/success-auto-inr-180.html",
        "/success-auto-inr-365.html",
        "/success-auto-usd-7.html",
        "/success-auto-usd-20.html",
        "/success-auto-usd-30.html",
        "/success-auto-usd-60.html",
        "/success-auto-usd-90.html",
        "/success-auto-usd-180.html",
        "/success-auto-usd-365.html"
    ]
    
    # Category content pages
    category_content = [
        "/action/movies.html",
        "/action/web-series.html",
        "/bengali/movies.html",
        "/bengali/web-series.html",
        "/bhojpuri/movies.html",
        "/bhojpuri/web-series.html",
        "/comedy/movies.html",
        "/comedy/web-series.html",
        "/crime/movies.html",
        "/crime/web-series.html",
        "/documentary/movies.html",
        "/documentary/web-series.html",
        "/drama/movies.html",
        "/drama/web-series.html",
        "/english/movies.html",
        "/english/web-series.html",
        "/fantasy/movies.html",
        "/fantasy/web-series.html",
        "/gay/movies.html",
        "/gay/web-series.html",
        "/gujarati/movies.html",
        "/gujarati/web-series.html",
        "/hindi/movies.html",
        "/hindi/web-series.html",
        "/international/movies.html",
        "/international/web-series.html",
        "/horror/movies.html",
        "/horror/web-series.html",
        "/kannada/movies.html",
        "/kannada/web-series.html",
        "/lesbian/movies.html",
        "/lesbian/web-series.html",
        "/lgbtq/movies.html",
        "/lgbtq/web-series.html",
        "/malayalam/movies.html",
        "/malayalam/web-series.html",
        "/marathi/movies.html",
        "/marathi/web-series.html",
        "/mystery/movies.html",
        "/mystery/web-series.html",
        "/punjabi/movies.html",
        "/punjabi/web-series.html",
        "/romantic/movies.html",
        "/romantic/web-series.html",
        "/reality/movies.html",
        "/reality/web-series.html",
        "/sports/movies.html",
        "/sports/web-series.html",
        "/tamil/movies.html",
        "/tamil/web-series.html",
        "/telugu/movies.html",
        "/telugu/web-series.html",
        "/thrillers/movies.html",
        "/thrillers/web-series.html"
    ]
    
    # Blog pages
    blog_pages = [
        "/blogs/10-ways-to-show-loyalty-in-your-lesbian-relationship.html",
        "/blogs/a-closer-look-at-eortvs-portrayal-of-bisexual-pansexual-love.html",
        "/blogs/balance-relationship.html",
        "/blogs/being-homo.html",
        "/blogs/best-crime-web-series.html",
        "/blogs/bullying-and-harassment-among-the-lgbt-youth.html",
        "/blogs/celebrating-lgbtq-love.html",
        "/blogs/celebrating-pride-through-eortv-stories.html",
        "/blogs/challenges-faced-by-the-sexual-minorities.html",
        "/blogs/coming-out-process.html",
        "/blogs/coming-out.html",
        "/blogs/cuba-country-legalised-same-sex-marriage.html",
        "/blogs/eortv-most-popular-web-series-a-complete-guide.html",
        "/blogs/eortv-shines-light-on-diversity-in-sports.html",
        "/blogs/eortv-vs-netflix-amazon-prime-and-other-ott-giants-whats-the-difference.html",
        "/blogs/from-taboo-to-mainstream-the-journey-of-lgbtq-love-stories-in-eortv.html",
        "/blogs/game-of-the-sexes.html",
        "/blogs/gender-identify.html",
        "/blogs/gender-socialization-at-home.html",
        "/blogs/given-the-situation-how-should-we-move-forward.html",
        "/blogs/goa-pride-festival-in-collaboration-with-eortv.html",
        "/blogs/government-position-on-lgbtqia.html",
        "/blogs/greater-engagement-among-members-of-gay.html",
        "/blogs/guide-to-navigating-open-lgbt-relationships.html",
        "/blogs/homo-in-india.html",
        "/blogs/homosexuality-in-society.html",
        "/blogs/how-eortv-challenges-stereotypes-of-lgbt-love.html",
        "/blogs/how-eortv-depicts-complexities-of-lgbt-love.html",
        "/blogs/how-eortv-depicts-the-intersectionality-of-lgbtq-love.html",
        "/blogs/how-eortv-is-competing-in-the-crowded-ott-market-what-sets-it-apart.html",
        "/blogs/how-eortv-is-supporting-independent-filmmakers-in-the-ott-space.html",
        "/blogs/how-eortv-lbgtq-love-stories-are-challenging-the-status-quo.html",
        "/blogs/how-eortvs-creative-team-brings-authenticity-to-their-lgbtq-love-stories.html",
        "/blogs/how-eortvs-queer-love-stories-are-changing-hearts-and-minds.html",
        "/blogs/how-have-rights-for-lgbt-changed-over-the-past-years.html",
        "/blogs/i-love-us-2-will-feature-the-song-ishq-jo-tumse-hua-by-samrat-sarkar.html",
        "/blogs/i-love-us-3-breaking-barriers-and-promoting-inclusivity-through-diverse-representation-in-media.html",
        "/blogs/i-love-us-lead-in-drishyam-2.html",
        "/blogs/iconic-lgtb-love-stories.html",
        "/blogs/importance-of-diversity-and-inclusion-in-sports.html",
        "/blogs/importance-of-mombian.html",
        "/blogs/international-day-for-girl-child.html",
        "/blogs/leave-no-one-behind-making-mental-health-care-accessible-to-lgbtqia.html",
        "/blogs/lessons-from-eortv.html",
        "/blogs/lgbtq-rights-in-80s-90s.html",
        "/blogs/mombian-a-celebration-of-love-and-family.html",
        "/blogs/must-watch-lesbian-webseries.html",
        "/blogs/my-girlfriend-and-i.html",
        "/blogs/navigating-the-dating-scene-as-an-lgbtq-individual.html",
        "/blogs/perspective-of-lgbtq-employees.html",
        "/blogs/power-of-love.html",
        "/blogs/prince-manvendra-singh-gohils-journey.html",
        "/blogs/right-to-marry.html",
        "/blogs/role-of-empathy-in-building-strong-lgbt-relationships.html",
        "/blogs/section-377.html",
        "/blogs/supportive-community.html",
        "/blogs/suspense-thriller-webseries-to-keep-you-on-the-edge.html",
        "/blogs/sydney-mardi-gras.html",
        "/blogs/tamil-nadu-step-for-betterment-of-lgbtq.html",
        "/blogs/the-challenges-of-intimacy.html",
        "/blogs/the-differenceibetween-sexual-orientation-and-gender-identity.html",
        "/blogs/the-different-forms-of-lgbt-love.html",
        "/blogs/the-effects-of-violence-in-the-lgbt-community.html",
        "/blogs/the-first-lesbian-wedding-will-be-shown-on-eortv-app-i-love-us-season-2.html",
        "/blogs/the-future-of-content-consumption-why-ott-platforms-like-eortv-are-the-future.html",
        "/blogs/the-future-of-lesbianism.html",
        "/blogs/the-growth-of-the-ott-industry-why-eortv-is-positioned-for-success.html",
        "/blogs/the-impact-of-eortv.html",
        "/blogs/the-impact-of-trauma-on-lgbtq-relationship.html",
        "/blogs/the-most-addictive-eortv-web-series.html",
        "/blogs/the-role-of-friendship.html",
        "/blogs/the-role-of-vulnerability-in-love-and-connection.html",
        "/blogs/top-5-must-watch-shows-on-eortv-your-ultimate-streaming-guide.html",
        "/blogs/top-5-webseries-that-deserve-your-attention.html",
        "/blogs/top-indian-webseries-you-need-to-watch.html",
        "/blogs/tu-meri-aashiqui-hai.html",
        "/blogs/un-trying-to-unit-lgbtqia.html",
        "/blogs/what-indian-ott-platforms-offer-that-international-ott-services-cant-a-closer-look-at-eortv.html",
        "/blogs/what-makes-eortv-the-ideal-ott-platform-for-binge-watching.html",
        "/blogs/why-eortv-webseries-depiction-of-lgbtq-characters-is-a-game-changer.html",
        "/blogs/why-gay-marriage-is-still-a-problem.html"
    ]
    
    @task
    def browse_main_pages(self):
        page = random.choice(self.main_pages)
        self.client.get(page)
    
    @task
    def browse_genres(self):
        genre = random.choice(self.genres)
        self.client.get(genre)
    
    @task
    def browse_languages(self):
        language = random.choice(self.languages)
        self.client.get(language)
    
    @task
    def browse_lgbtq_content(self):
        page = random.choice(self.lgbtq_pages)
        self.client.get(page)
    
    @task
    def browse_original_content(self):
        content = random.choice(self.original_content)
        self.client.get(content)
    
    @task
    def view_documents(self):
        doc = random.choice(self.documents)
        self.client.get(doc)
    
    @task
    def view_email_templates(self):
        template = random.choice(self.email_templates)
        self.client.get(template)
    
    @task
    def view_success_pages(self):
        success_page = random.choice(self.success_pages)
        self.client.get(success_page)
    
    @task
    def browse_category_content(self):
        category = random.choice(self.category_content)
        self.client.get(category)
    
    @task
    def read_blogs(self):
        blog = random.choice(self.blog_pages)
        self.client.get(blog)