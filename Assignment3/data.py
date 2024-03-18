# Author: Marvin Neoh

countries_and_capitals = (
    ['Afghanistan', 'Kabul'], ['Albania', 'Tirana (Tirane)'], ['Algeria', 'Algiers'], ['Andorra', 'Andorra la Vella'],
    ['Angola', 'Luanda'], ['Antigua and Barbuda', "Saint John's"], ['Argentina', 'Buenos Aires'],
    ['Armenia', 'Yerevan'], ['Australia', 'Canberra'], ['Austria', 'Vienna'], ['Azerbaijan', 'Baku'],
    ['Bahamas', 'Nassau'], ['Bahrain', 'Manama'], ['Bangladesh', 'Dhaka'], ['Barbados', 'Bridgetown'],
    ['Belarus', 'Minsk'], ['Belgium', 'Brussels'], ['Belize', 'Belmopan'], ['Benin', 'Porto Novo'],
    ['Bhutan', 'Thimphu'], ['Bolivia', 'Sucre'], ['Bosnia and Herzegovina', 'Sarajevo'], ['Botswana', 'Gaborone'],
    ['Brazil', 'Brasilia'], ['Brunei', 'Bandar Seri Begawan'], ['Bulgaria', 'Sofia'], ['Burkina Faso', 'Ouagadougou'],
    ['Burundi', 'Gitega'], ['Cambodia', 'Phnom Penh'], ['Cameroon', 'Yaounde'], ['Canada', 'Ottawa'],
    ['Cape Verde', 'Praia'], ['Central African Republic', 'Bangui'], ['Chad', "N'Djamena"], ['Chile', 'Santiago'],
    ['China', 'Beijing'], ['Colombia', 'Bogota'], ['Comoros', 'Moroni'],
    ['Congo, Democratic Republic of the', 'Kinshasa'], ['Congo, Republic of the', 'Brazzaville'],
    ['Costa Rica', 'San Jose'], ["Cote d'Ivoire (Ivory Coast)", 'Yamoussoukro'], ['Croatia', 'Zagreb'],
    ['Cuba', 'Havana'], ['Cyprus', 'Nicosia'], ['Czech Republic (Czechia)', 'Prague'], ['Denmark', 'Copenhagen'],
    ['Djibouti', 'Djibouti'], ['Dominica', 'Roseau'], ['Dominican Republic', 'Santo Domingo'], ['East Timor', 'Dili'],
    ['Ecuador', 'Quito'], ['Egypt', 'Cairo'], ['El Salvador', 'San Salvador'], ['England', 'London'],
    ['Equatorial Guinea', 'Malabo'], ['Eritrea', 'Asmara'], ['Estonia', 'Tallinn'], ['Eswatini (Swaziland)', 'Mbabana'],
    ['Ethiopia', 'Addis Ababa'], ['Federated States of Micronesia', 'Palikir'], ['Fiji', 'Suva'],
    ['Finland', 'Helsinki'], ['France', 'Paris'], ['Gabon', 'Libreville'], ['Gambia', 'Banjul'], ['Georgia', 'Tbilisi'],
    ['Germany', 'Berlin'], ['Ghana', 'Accra'], ['Greece', 'Athens'], ['Grenada', "Saint George's"],
    ['Guatemala', 'Guatemala City'], ['Guinea', 'Conakry'], ['Guinea-Bissau', 'Bissau'], ['Guyana', 'Georgetown'],
    ['Haiti', 'Port au Prince'], ['Honduras', 'Tegucigalpa'], ['Hungary', 'Budapest'], ['Iceland', 'Reykjavik'],
    ['India', 'New Delhi'], ['Indonesia', 'Jakarta'], ['Iran', 'Tehran'], ['Iraq', 'Baghdad'], ['Ireland', 'Dublin'],
    ['Israel', 'Jerusalem'], ['Italy', 'Rome'], ['Jamaica', 'Kingston'], ['Japan', 'Tokyo'], ['Jordan', 'Amman'],
    ['Kazakhstan', 'Nur-Sultan'], ['Kenya', 'Nairobi'], ['Kiribati', 'Tarawa Atoll'], ['Kosovo', 'Pristina'],
    ['Kuwait', 'Kuwait City'], ['Kyrgyzstan', 'Bishkek'], ['Laos', 'Vientiane'], ['Latvia', 'Riga'],
    ['Lebanon', 'Beirut'], ['Lesotho', 'Maseru'], ['Liberia', 'Monrovia'], ['Libya', 'Tripoli'],
    ['Liechtenstein', 'Vaduz'], ['Lithuania', 'Vilnius'], ['Luxembourg', 'Luxembourg'], ['Madagascar', 'Antananarivo'],
    ['Malawi', 'Lilongwe'], ['Malaysia', 'Kuala Lumpur'], ['Maldives', 'Male'], ['Mali', 'Bamako'],
    ['Malta', 'Valletta'], ['Marshall Islands', 'Majuro'], ['Mauritania', 'Nouakchott'], ['Mauritius', 'Port Louis'],
    ['Mexico', 'Mexico City'], ['Moldova', 'Chisinau'], ['Monaco', 'Monaco'], ['Mongolia', 'Ulaanbaatar'],
    ['Montenegro', 'Podgorica'], ['Morocco', 'Rabat'], ['Mozambique', 'Maputo'], ['Myanmar (Burma)', 'Nay Pyi Taw'],
    ['Namibia', 'Windhoek'], ['Nauru', 'No official capital'], ['Nepal', 'Kathmandu'], ['Netherlands', 'Amsterdam'],
    ['New Zealand', 'Wellington'], ['Nicaragua', 'Managua'], ['Niger', 'Niamey'], ['Nigeria', 'Abuja'],
    ['North Korea', 'Pyongyang'], ['North Macedonia (Macedonia)', 'Skopje'], ['Northern Ireland', 'Belfast'],
    ['Norway', 'Oslo'], ['Oman', 'Muscat'], ['Pakistan', 'Islamabad'], ['Palau', 'Melekeok'], ['Panama', 'Panama City'],
    ['Papua New Guinea', 'Port Moresby'], ['Paraguay', 'Asuncion'], ['Peru', 'Lima'], ['Philippines', 'Manila'],
    ['Poland', 'Warsaw'], ['Portugal', 'Lisbon'], ['Qatar', 'Doha'], ['Romania', 'Bucharest'], ['Russia', 'Moscow'],
    ['Rwanda', 'Kigali'], ['Saint Kitts and Nevis', 'Basseterre'], ['Saint Lucia', 'Castries'],
    ['Saint Vincent and the Grenadines', 'Kingstown'], ['Samoa', 'Apia'], ['San Marino', 'San Marino'],
    ['Sao Tome and Principe', 'Sao Tome'], ['Saudi Arabia', 'Riyadh'], ['Scotland', 'Edinburgh'], ['Senegal', 'Dakar'],
    ['Serbia', 'Belgrade'], ['Seychelles', 'Victoria'], ['Sierra Leone', 'Freetown'], ['Singapore', 'Singapore'],
    ['Slovakia', 'Bratislava'], ['Slovenia', 'Ljubljana'], ['Solomon Islands', 'Honiara'], ['Somalia', 'Mogadishu'],
    ['South Africa', 'Pretoria, Bloemfontein, Cape Town'], ['South Korea', 'Seoul'], ['South Sudan', 'Juba'],
    ['Spain', 'Madrid'], ['Sri Lanka', 'Colombo'], ['Sudan', 'Khartoum'], ['Suriname', 'Paramaribo'],
    ['Sweden', 'Stockholm'], ['Switzerland', 'Bern'], ['Syria', 'Damascus'], ['Taiwan', 'Taipei'],
    ['Tajikistan', 'Dushanbe'], ['Tanzania', 'Dodoma'], ['Thailand', 'Bangkok'], ['Togo', 'Lome'],
    ['Tonga', "Nuku'alofa"], ['Trinidad and Tobago', 'Port of Spain'], ['Tunisia', 'Tunis'], ['Turkey', 'Ankara'],
    ['Turkmenistan', 'Ashgabat'], ['Tuvalu', 'Funafuti'], ['Uganda', 'Kampala'], ['Ukraine', 'Kiev'],
    ['United Arab Emirates', 'Abu Dhabi'], ['United Kingdom', 'London'], ['United States', 'Washington D.C.'],
    ['Uruguay', 'Montevideo'], ['Uzbekistan', 'Tashkent'], ['Vanuatu', 'Port Vila'], ['Vatican City', 'Vatican City'],
    ['Venezuela', 'Caracas'], ['Vietnam', 'Hanoi'], ['Wales', 'Cardiff'], ['Yemen', "Sana'a"], ['Zambia', 'Lusaka'],
    ['Zimbabwe', 'Harare']
)

def main():
    """
    This function does nothing
    """
    print('This function does nothing, do not call this function')


if __name__ == "__main__":
    main()
