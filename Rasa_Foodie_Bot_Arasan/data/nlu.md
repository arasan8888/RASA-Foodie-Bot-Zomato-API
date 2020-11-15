## intent:affirm
- yes
- yup
- yep
- yeah
- ya
- indeed
- that's right
- ok
- okay
- cool
- sure
- super
- wonderful
- excellent
- right
- alright
- thank you
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- thanks

## intent:deny
- no
- nope
- no thanks
- no thank you
- not required
- no need
- not needed
- please dont
- please don't
- leave it
- bad choice
- wrong
- nah
- noo

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- hai
- good afternoon
- hullo
- hiya
- hola
- ola
- good morning
- good evening
- dear sir
- hi
- hi
- hello

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [bengaluru](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [kanpur](location)
- i am looking for an [north indian](cuisine)
- search for restaurants
- anywhere in the [chandigarh](location)
- I am looking for [south indian](cuisine) food
- I am looking a restaurant in [mangalore](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [chennai](location)
- [mexican](cuisine)
- [american](cuisine)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican](cuisine)
- can you book a table in [patna](location) in a [moderate](price:below_700) price range with [north indian](cuisine) food
- [mumbai](location) [italian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurant in [Bengaluru](location)
- [delhi](location)
- [Chinese](cuisine:chinese)
- show me restaurants
- [coimbatore](location)
- [american](cuisine)
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [Bengaluru](location)
- find a [mexican](cuisine) place to eat in [mumbai](location)
- need to grab [american](cuisine) food
- please find me a [chinese](cuisine:chinese) restaurant in [mumbai](location:mumbai) with price for two people [more than 700](price:above_700)
- show me some restaurants in [lucknow](location) with price range at [300-700](price:below_700) specializing in [North Indian](cuisine)
- get me a list of [mexican](cuisine) restaurants in [chennai](location) for a budget of [more than rs.700](price:above_700)
- please find me a [chinese](cuisine) restaurant in [mumbai](location) with average cost for two people [above 700](price:above_700)

## intent:price_check
- [less than 300](price:below_300)
- [more than 300](price:below_700)
- [more than 700](price:above_700)
- [expensive](price:above_700)
- [extravagant](price:above_700)
- [low](price:below_300)
- [medium](price:below_700)
- [high](price:above_700)
- [below 300](price:below_300)
- [greater than 300 and less than 700](price:below_700)
- [below_300](price)
- [below_700](price)
- [above_700](price)
- [reasonable](price:below_700)
- [moderate](price:below_700)
- [average](price:below_700)
- [normal](price:below_700)
- [simple](price:below_300)
- [300-700](price:below_700) range
- [300 to 700](price:below_700) range
- [<300](price:below_300)
- [>700](price:above_700)

## intent:get_cuisine
- [Italian](cuisine:italian)
- [Chinese](cuisine:chinese)
- [Mexican](cuisine:mexican)
- [American](cuisine:american)
- [north indian](cuisine)
- [south indian](cuisine)
- [North Indian](cuisine:north indian)
- [South Indian](cuisine:south indian)
- I would like to get [chinese](cuisine:chinese)
- I prefer [mexican](cuisine:mexican)
- i'd prefer [american](cuisine:american)
- i like [italian](cuisine:italian)


## synonym:Delhi
- New Delhi
- dilli
- old delhi
- capital of india

## synonym:Mumbai
- bombay
- bombai
- Bombay

## synonym:chennai
- madras
- Madras
- chenai
- chenna

## synonym:Prayagraj
- allahabad
- Allahabad

## synonym:Tiruchirappalli
- trichy
- tiruchirapalli
- tiruchirappali

# synonym:Jabalpur
- Jubbulpore

# synonym:Kanpur
- khanpur
- cawnpore

# synonym:Vadodara
- Baroda
- baroda

## synonym:Bengaluru
- bangalore
- bangalor
- Bangalore

## synonym:Thiruvananthapuram
- trivandrum
- Trivandrum

## synonym:gurgaon
- Gurugram
- gurugram

## synonym:kochi
- Cochin
- cochin

## synonym:thanjavur
- Tanjore
- tanjore

## synonym:kolkata
- calcutta
- Calcutta

## synonym:Mysore
- mysuru
- Mysuru

## synonym:mangalore
- Mangaluru
- mangaluru

## synonym:Pondicherry
- Puducherry
- puducherry

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:american
- usa
- americen
- america

## synonym:italian
- Italian
- italia

## synonym:mexican
- mexicana
- mexica

## synonym:north indian
- north
- northindian
- noth indian


## synonym:south indian
- south
- soth indian
- southindian

## synonym:below_700
- moderate
- medium
- average



## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## regex:email
- (\S+@\S+\.[a-zA-Z]+)

## intent:get_email
- Yes, send it to my email at [akash.sisty08@gmail.com](email)
- Send to [akash.sisty08@gmail.com](email)
- [abcd1234@domain.com](email)
- Yes, please send it to [crazy.cat@gmail.com](email)
- [rahul.dhawan_08@gmail.com](email)
- [some_name02@gmail.com](email)
- yeah, send to [pingoo_igloo@yahoo.com](email)
- send to me at [deva.prasad@domain.com](email)
- send to [deva.prasad@outlook.com](email)
- send to [krishna.deva@google.com](email)
- [arasan8888@gmail.com](email)
