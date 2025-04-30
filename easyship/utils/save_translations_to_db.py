from easyship.utils import translate_content
from easyship.models.multilanguage import MultiLanguages
from decimal import Decimal
from loguru import logger

homeContent = [
    "Welcome to",
    "Your reliable partner for global trade services.",
    "Request a Free Quote Today",
    "We ship your goods safely overseas",
    "While we deal with the oceans of paperwork!",
    "Welcome to ADI LAXMI EXPORTS, where global trade meets exceptional service. Since 2021, we have been a leading player in the export-import industry, dedicated to bridging markets and creating seamless trade experiences. Our mission is to connect businesses across borders with ease and efficiency. We strive to provide unparalleled expertise in navigating complex international markets, ensuring that your products reach their destinations smoothly and securely.",

    "Our Services",
    "Global Shipping",
    "Fast and reliable shipping services to over 150 countries worldwide.",
    "Warehousing",
    "Secure and efficient warehousing solutions for your valuable goods.",
    "Export Consultation",
    "Expert consultation services to streamline your export processes.",
    "Trade Partnerships", 
    "Building strong trade partnerships with global businesses",


    "Contact Us",
    "Get in Touch",
    "We'd love to hear from you. Whether you have a question about services, pricing, or anything else, our team is ready to answer all your questions.",
    "179(333) Alipur Road, North 24 Parganas, Kolkata, India",
    "+91 62908 73065",
    "info@adilaxmiexports.com",


    "Name",
    "Your name",
    "Email",
    "Your email",
    "Message",
    "Your Message",
    "Send",


    "Certificates",

    "Exports",
    "Diamond and Gold ",
    "Jwellery Products",
    "Precious and Semi Precious Stones",

    "About",
    "Company",
    "Team",
    "Careers",
    "Adi Laxmi Exports",
    "Leading Diamond  and Leather Product exporters in India must comprehend the needs and desires of their customers in order to provide goods of unparalleled quality and remarkable value."

]

navContent = [
    "Home",
    "Export Services",
    "Certificates",
    "Contact Us",
    "About",

]

aboutContent = [
    "About Us",
    "At ADI LAXMI EXPORTS, we bridge continents and connect businesses with seamless ocean freight services. Discover our story, values, and commitment to excellence in the global shipping industry.",


    "Who We Are",
    "Welcome to ADI LAXMI EXPORTS, where global trade meets exceptional service. Since 2021, we have been a leading player in the export-import industry, dedicated to bridging markets and creating seamless trade experiences.",

    "Our Mission",
    "Our mission is to redefine ocean freight by delivering unparalleled service, innovation, and reliability.We are committed to ensuring that every shipment is a seamless experience, providing our clients with peace of mind and a competitive edge in their markets.",

    "We believe in building long - term relationships with our clients, partners, and communities by upholding the highest standards of integrity, transparency, and sustainability.",

    "Our Core Values",
    "Integrity:",
    "We operate with honesty and uphold the highest ethical standards in every aspect of our business.",
    "Innovation:",
    "We embrace change and continuously seek new ways to improve our services and operations.",
    " Excellence: ",
    "We strive for excellence in everything we do, from customer service to operational efficiency.",
    "Sustainability:",
    " We are committed to reducing our environmental impact and promoting sustainable practices in the shipping industry.",
    "Teamwork:",
    "We believe in the power of collaboration and work closely with our clients, partners, and employees to achieve common goals.",
    "Our Leadership",
    "Our leadership team is composed of seasoned professionals with extensive experience in the shipping and logistics industry.Their vision, expertise, and commitment to excellence guide ADI LAXMI EXPORTS in delivering superior service and driving innovation in ocean freight.",
    "Partner with Us",
    "Whether you are a small business looking to expand globally or a large corporation seeking a reliable shipping partner, ADI LAXMI EXPORTS is here to support your growth. We offer customized solutions tailored to your specific needs, ensuring that your cargo reaches its destination safely and on time.",
    "Contact us today to learn more about how we can help your business succeed in the global market.",
    "Contact Us",
    "179(333) Alipur Road, North 24 Parganas, Kolkata, India",
    "+91 62908 73065",
    "info @adilaxmiexports.com",


    "Home",
    "Export Services",
    "Certificates",
    "Contact Us",
    "About"
]



languages = [
    "af",
    "sq",
    "am",
    "ar",
    "hy",
    "az",
    "eu",
    "be",
    "bn",
    "bs",
    "bg",
    "ca",
    "ceb",
    "ny",
    "zh-cn",
    "zh-tw",
    "co",
    "hr",
    "cs",
    "da",
    "nl",
    "en",
    "eo",
    "et",
    "tl",
    "fi",
    "fr",
    "fy",
    "gl",
    "ka",
    "de",
    "el",
    "gu",
    "ht",
    "ha",
    "haw",
    "iw",
    "he",
    "hi",
    "hmn",
    "hu",
    "is",
    "ig",
    "id",
    "ga",
    "it",
    "ja",
    "jw",
    "kn",
    "kk",
    "km",
    "ko",
    "ku",
    "ky",
    "lo",
    "la",
    "lv",
    "lt",
    "lb",
    "mk",
    "mg",
    "ms",
    "ml",
    "mt",
    "mi",
    "mr",
    "mn",
    "my",
    "ne",
    "no",
    "or",
    "ps",
    "fa",
    "pl",
    "pt",
    "pa",
    "ro",
    "ru",
    "sm",
    "gd",
    "sr",
    "st",
    "sn",
    "sd",
    "si",
    "sk",
    "sl",
    "so",
    "es",
    "su",
    "sw",
    "sv",
    "tg",
    "ta",
    "te",
    "th",
    "tr",
    "uk",
    "ur",
    "ug",
    "uz",
    "vi",
    "cy",
    "xh",
    "yi",
    "yo",
    "zu",
]

contents = {
    "nav":navContent,
    "home": homeContent,
    "about": aboutContent,
}

def translate_and_save_language(tag):
    try:
        all_langs = get_all_langugaees_from_db()
        for language in languages:
            logger.info("Language to Translate {0}".format(language))
            if Decimal(tag) > Decimal(all_langs["tag"])  and language in all_langs["langs"]:
                logger.info("Checking If The Content of Language {0} is Presnt in DB".format(language))
                multilanguage_obj = MultiLanguages.objects.get(language = language)
                if multilanguage_obj:
                    navResult = translate_content(language=language,content=contents["nav"])
                    homeResult = translate_content(language=language,content=contents["home"])
                    aboutResult = translate_content(language=language,content=contents["about"])
                    multilanguage_obj.navcontent = navResult
                    multilanguage_obj.homecontent = homeResult
                    multilanguage_obj.aboutcontent = aboutResult
                    logger.info("Checking If The Content of Language {0} is Presnt in DB and Updating".format(language))
                    multilanguage_obj.save()
            elif language not in all_langs["langs"]:
                navResult = translate_content(language=language,content=contents["nav"])
                homeResult = translate_content(language=language,content=contents["home"])
                aboutResult = translate_content(language=language,content=contents["about"])
                logger.info("Checking If The Content of Language {0} is Not Presnt in DB and Saving the Content".format(language))
                multiLAnguageObject = MultiLanguages(
                    language=language,
                    navcontent = navResult,
                    homecontent = homeResult,
                    aboutcontent = aboutResult,
                )
                multiLAnguageObject.save()
            else:
                logger.info("Skipping DB Updating/Saving for language {0}".format(language))
    except Exception as e:
        logger.error("Error is Database Update: Error : {0}".format(e))
        raise Exception
    

def get_all_langugaees_from_db():
    all_languages = []
    lang_objs = MultiLanguages.objects.all()
    for lang_obj in lang_objs:
        all_languages.append(lang_obj.language)
    
    return {"langs": all_languages, "tag": lang_objs[0].tag}
            
        



            
