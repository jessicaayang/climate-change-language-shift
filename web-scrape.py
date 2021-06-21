# Import required modules
import newspaper
  
# Define list of urls
list_of_articles_1980 = [
'https://www.nytimes.com/1981/04/17/opinion/climate-and-co-2.html?searchResultPosition=3',
'https://www.nytimes.com/1983/10/21/us/excerpts-from-the-climate-report.html?searchResultPosition=4',
'https://www.nytimes.com/1982/04/23/us/large-volcanic-cloud-could-change-climate.html?searchResultPosition=5',
'https://www.nytimes.com/1984/06/08/us/center-to-study-shifts-in-climate.html?searchResultPosition=6',
'https://www.nytimes.com/1982/07/13/science/science-watch-dead-snails-reveal-climate.html?searchResultPosition=8',
'https://www.nytimes.com/1981/08/11/us/climate-cycles-studied-in-effort-to-curb-drought.html?searchResultPosition=9',
'https://www.nytimes.com/1985/12/11/us/action-is-urged-to-avert-global-climate-shift.html?searchResultPosition=10',
'https://www.nytimes.com/1982/01/07/us/warming-of-world-s-climate-expected-to-begin-in-the-80-s.html?searchResultPosition=13',
'https://www.nytimes.com/1985/07/28/us/climate-shift-laid-to-core-of-earth.html?searchResultPosition=11',
'https://www.nytimes.com/1980/09/02/archives/ancient-tree-rings-tell-a-tale-of-past-and-future-droughts-tree.html?searchResultPosition=16',
'https://www.nytimes.com/1984/01/03/science/report-urges-steps-to-slow-down-climate-warming.html?searchResultPosition=34',
'https://www.nytimes.com/1982/07/21/us/researchers-renew-warning-on-effects-of-global-warming.html?searchResultPosition=45',
'https://www.nytimes.com/1988/12/28/opinion/pseudoscientific-hot-air.html?searchResultPosition=1',
'https://www.nytimes.com/1988/12/25/weekinreview/the-world-suddenly-the-world-itself-is-a-world-issue.html?searchResultPosition=2',
'https://www.nytimes.com/1988/12/13/science/science-watch-cows-and-the-climate.html?searchResultPosition=3',
'https://www.nytimes.com/1988/12/07/us/ferocious-storms-and-drought-seen.html?searchResultPosition=4',
'https://www.nytimes.com/1988/11/26/us/common-ground-seen-on-warming-of-globe.html?searchResultPosition=5',
'https://www.nytimes.com/1988/10/20/us/draft-report-on-global-warming-foresees-environmental-havoc-in-us.html?searchResultPosition=7',
'https://www.nytimes.com/1988/10/02/weekinreview/ideas-trends-tough-choices-to-make-for-power-without-pollution.html?searchResultPosition=11',
'https://www.nytimes.com/1988/09/20/science/the-environment-forests-sought-to-counter-greenhouse-effect.html?searchResultPosition=12',
'https://www.nytimes.com/1988/09/04/weekinreview/ideas-trends-was-that-a-greenhouse-effect-it-depends-on-your-theory.html?searchResultPosition=13',
'https://www.nytimes.com/1988/08/28/business/fighting-the-greenhouse-effect.html?searchResultPosition=14',
'https://www.nytimes.com/1988/08/23/science/his-bold-statement-transforms-the-debate-on-greenhouse-effect.html?searchResultPosition=16',
'https://www.nytimes.com/1988/08/16/science/scientists-dream-up-bold-remedies-for-ailing-atmosphere.html?searchResultPosition=17',
'https://www.nytimes.com/1988/07/27/opinion/foreign-affairs-the-next-big-crisis.html?searchResultPosition=18%27'
]

list_of_articles_1990 = [
'https://www.nytimes.com/1995/12/19/science/glaciers-are-star-witnesses-to-the-history-of-earth-s-climate.html?searchResultPosition=1',
'https://www.nytimes.com/1995/12/01/world/talk-about-weather-un-says-people-do-something-about-it.html?searchResultPosition=2',
'https://www.nytimes.com/1995/11/08/world/scientists-say-rain-forests-lower-levels-of-global-carbon-dioxide.html?searchResultPosition=7',
'https://www.nytimes.com/1995/10/25/world/un-warns-against-delay-in-cutting-carbon-dioxide-emissions.html?searchResultPosition=9',
'https://www.nytimes.com/1995/10/10/science/price-of-global-warming-debate-weighs-dollars-and-cents.html?searchResultPosition=10',
'https://www.nytimes.com/1995/09/26/science/in-rain-and-temperature-data-new-signs-of-global-warming.html?searchResultPosition=11',
'https://www.nytimes.com/1995/09/24/us/white-house-considers-toughening-its-anti-emissions-program.html?searchResultPosition=12',
'https://www.nytimes.com/1995/09/18/world/scientists-say-earth-s-warming-could-set-off-wide-disruptions.html?searchResultPosition=13',
'https://www.nytimes.com/1995/09/18/opinion/global-warming-heats-up.html?searchResultPosition=14',
'https://www.nytimes.com/1995/09/18/world/us-utilities-helping-czechs-to-curb-greenhouse-gases-and-air-pollutants.html?searchResultPosition=15',
'https://www.nytimes.com/1995/09/10/world/global-warming-experts-call-human-role-likely.html?searchResultPosition=16',
'https://www.nytimes.com/1995/09/09/opinion/chinas-power-to-harm-the-planet.html?searchResultPosition=17',
'https://www.nytimes.com/1995/08/22/business/us-industries-oppose-emission-proposals.html?searchResultPosition=18',
'https://www.nytimes.com/1993/12/09/us/new-study-challenges-theory-on-climate-change.html?searchResultPosition=21',
'https://www.nytimes.com/1995/09/26/opinion/l-global-warming-unfortunately-is-all-too-real-044395.html?searchResultPosition=27',
'https://www.nytimes.com/1995/09/19/opinion/l-global-warming-remains-unproved-386995.html?searchResultPosition=30',
'https://www.nytimes.com/1995/05/23/science/more-extremes-found-in-weather-pointing-to-greenhouse-gas-effect.html?searchResultPosition=31',
'https://www.nytimes.com/1990/04/24/science/clouds-are-yielding-clues-to-changes-in-climate.html?searchResultPosition=34',
'https://www.nytimes.com/1995/04/11/science/climate-talks-enter-harder-phase-of-cutting-back-emissions.html?searchResultPosition=35',
'https://www.nytimes.com/1990/05/15/science/science-watch-methane-and-climate.html?searchResultPosition=37',
'https://www.nytimes.com/1994/09/20/science/emissions-must-be-cut-to-avert-shift-in-climate-panel-says.html?searchResultPosition=39',
'https://www.nytimes.com/1990/09/30/business/l-climate-change-and-coal-883290.html?searchResultPosition=44',
'https://www.nytimes.com/1991/02/15/world/talks-on-climate-end-with-accord.html?searchResultPosition=45',
'https://www.nytimes.com/1990/06/02/us/critics-say-draft-report-on-climate-shift-ignores-urgency-of-problem.html?searchResultPosition=46',
'https://www.nytimes.com/1991/07/02/science/science-watch-clues-to-the-climate-in-a-coral-reef.html?searchResultPosition=52'
]

list_of_articles_2000 = [
'https://www.nytimes.com/2009/12/28/opinion/28iht-edbowring.html?searchResultPosition=1',
'https://www.nytimes.com/2009/12/21/us/21caucus.html?searchResultPosition=5',
'https://www.nytimes.com/2009/12/08/business/global/08rbogbgc.html?searchResultPosition=6',
'https://www.nytimes.com/2009/12/14/science/earth/14bolivia.html?searchResultPosition=7',
'https://www.nytimes.com/2009/12/12/science/earth/12climate.html?searchResultPosition=8',
'https://www.nytimes.com/2009/11/23/business/energy-environment/23iht-green23.html?searchResultPosition=10',
'https://www.nytimes.com/2009/12/23/world/europe/23iht-climate.html?searchResultPosition=12',
'https://www.nytimes.com/2009/12/23/world/asia/23china.html?searchResultPosition=11',
'https://www.nytimes.com/2009/12/27/opinion/27lafolley.html?searchResultPosition=13',
'https://www.nytimes.com/2009/12/31/business/energy-environment/31carbon.html?searchResultPosition=14',
'https://www.nytimes.com/video/science/earth/1247466204300/ban-ki-moon-on-copenhagen-climate-deal.html?searchResultPosition=15',
'https://www.nytimes.com/2009/12/25/opinion/25fri2.html?searchResultPosition=16',
'https://www.nytimes.com/2009/12/20/science/earth/20accord.html?searchResultPosition=17',
'https://www.nytimes.com/video/multimedia/1247466194031/president-obama-on-a-climate-agreement.html?searchResultPosition=18',
'https://www.nytimes.com/2009/12/21/world/europe/21scene.html?searchResultPosition=20',
'https://www.nytimes.com/2006/12/14/business/recalculating-the-costs-of-global-climate-change.html?searchResultPosition=1',
'https://www.nytimes.com/2006/12/16/world/world-briefing-americas-inuit-climate-change-petition-rejected.html?searchResultPosition=3',
'https://www.nytimes.com/2006/12/30/business/travel-habits-must-change-to-make-a-big-difference-in-energy.html?searchResultPosition=6',
'https://www.nytimes.com/2006/12/27/opinion/27wed4.html?searchResultPosition=14',
'https://www.nytimes.com/2006/12/28/business/us-companies-explore-ways-to-profit-from-trading-credits-to-emit.html?searchResultPosition=16',
'https://www.nytimes.com/2008/12/11/world/europe/11climate.html?searchResultPosition=2',
'https://dotearth.blogs.nytimes.com/2008/12/01/climate-not-the-story-of-our-time/?searchResultPosition=3',
'https://www.nytimes.com/2008/12/28/opinion/28inglis.html?searchResultPosition=4',
'https://www.nytimes.com/2008/12/23/science/23labside1.html?searchResultPosition=9',
'https://www.nytimes.com/2008/12/13/world/13climate.html?searchResultPosition=13'
]

outF = open("WebScrapeOutFile.csv", "w", encoding="utf-8")

outF.write("Decade,Article1,Article2,Article3,Article4,Article5,Article6,Article7,Article8,"+
      "Article9,Article10,Article11,Article12,Article13,Article14,Article15,Article16,"+
      "Article17,Article18,Article19,Article20,Article21,Article22,Article23,Article24,Article25")
outF.write("\n")

i = 0
x="1980s,\""
for url in list_of_articles_1980:
    url_i = newspaper.Article(url="%s" % (url), language='en')
    url_i.download()
    url_i.parse()
    url_i.text=url_i.text.replace('“', '\'')
    url_i.text=url_i.text.replace('”', '\'')
    url_i.text=url_i.text.replace('"', '\'')
    if i < 24 :
        i += 1
        x=x+url_i.text+"\""+"," + "\""
    else:
        x=x+url_i.text+"\""

outF.write(x)
outF.write("\n")

i = 0
x="1990s,\""
for url in list_of_articles_1990:
    url_i = newspaper.Article(url="%s" % (url), language='en')
    url_i.download()
    url_i.parse()
    url_i.text=url_i.text.replace('“', '\'')
    url_i.text=url_i.text.replace('”', '\'')
    url_i.text=url_i.text.replace('"', '\'')
    if i < 24 :
        i += 1
        x=x+url_i.text+"\""+"," + "\""
    else:
        x=x+url_i.text+"\""

outF.write(x)
outF.write("\n")

i = 0
x="2000s,\""
for url in list_of_articles_2000:
    url_i = newspaper.Article(url="%s" % (url), language='en')
    url_i.download()
    url_i.parse()
    url_i.text=url_i.text.replace('“', '\'')
    url_i.text=url_i.text.replace('”', '\'')
    url_i.text=url_i.text.replace('"', '\'')
    if i < 24 :
        i += 1
        x=x+url_i.text+"\""+"," + "\""
    else:
        x=x+url_i.text+"\""

outF.write(x)
outF.write("\n")
outF.close()
