import datetime
import requests


def translate_event(event_type, event_class, event_title, event_text, image_url):
    if event_type == "STARTED":
        return {
                "event_type": event_type,
                "event_class": event_class,
                "event_title": "打印任务开始",
                "event_text": event_text,
                "image_url": image_url
                }

    elif event_type == "ENDED":
        if event_type == "SUCCESS":
            return {
                "event_type": event_type,
                "event_class": event_class,
                "event_title": "打印任务已完成",
                "event_text": event_text,
                "image_url": image_url
            }
        elif event_type == "WARNING":
            return {
                "event_type": event_type,
                "event_class": event_class,
                "event_title": "打印任务已取消",
                "event_text": event_text,
                "image_url": image_url
            }
        else:
            return {
                "event_type": event_type,
                "event_class": event_class,
                "event_title": event_title,
                "event_text": event_text,
                "image_url": image_url
            }

    elif event_type == "PRINTER_ERROR":
        return {
                "event_type": event_type,
                "event_class": event_class,
                "event_title": "打印机错误 " + event_title + " " + event_text,
                "event_text": event_text,
                "image_url": image_url
                }

    elif event_type == "RESUMED":
        return {
                "event_type": event_type,
                "event_class": event_class,
                "event_title": "打印任务恢复",
                "event_text": event_text,
                "image_url": image_url
                }

    elif event_type == "PAUSED":
        return {
                "event_type": event_type,
                "event_class": event_class,
                "event_title": "打印任务暂停",
                "event_text": event_text,
                "image_url": image_url
                }

    elif event_type == "ALERT_MUTED":
        return {
                "event_type": event_type,
                "event_class": event_class,
                "event_title": "检测已关闭",
                "event_text": event_text,
                "image_url": image_url
                }

    elif event_type == "FAILURE_ALERTED":
        return {
                "event_type": event_type,
                "event_class": event_class,
                "event_title": "检测到潜在故障",
                "event_text": event_text,
                "image_url": image_url
                }

    else:
        return {
                "event_type": event_type,
                "event_class": event_class,
                "event_title": "未知状态" + event_title + " " + event_text,
                "event_text": event_text,
                "image_url": image_url
                }


def send_msg(msg_url, msg, image_url):
    msg = f"{msg}"
    url = f"{msg_url}{msg}?icon={image_url}&url={image_url}"
    requests.get(url)
    print(f"{str(datetime.datetime.now())[:19]} 消息已推送至iPhone: {msg}")
    return 0


def request_event(url, token):
    payload = {}
    headers = {
        'Authorization': f'{token}'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    event_type = response.json()[0]["event_type"]
    event_class = response.json()[0]["event_class"]
    event_title = response.json()[0]["event_title"]
    event_text = response.json()[0]["event_text"]
    image_url = response.json()[0]["image_url"]

    return {
            "event_type": event_type,
            "event_class": event_class,
            "event_title": event_title,
            "event_text": event_text,
            "image_url": image_url
            }


def check_event(msg_url, event_url):
    event_tmp_list = [0]

    while True:
        event = request_event(event_url, obico_token)
        event_type = event["event_type"]
        event_class = event["event_class"]
        event_title = event["event_title"]
        event_text = event["event_text"]
        image_url = event["image_url"]

        if event_type != event_tmp_list[-1] and event_type is not None:
            event_tmp_list.append(event_type)
            print(f"{str(datetime.datetime.now())[:19]} 打印机状态已改变 当前状态：{event_type}")
            zh_msg = translate_event(event_type, event_class, event_title, event_text, image_url)

            msg = f"[{zh_msg["event_class"]}] {zh_msg["event_title"]}"
            send_msg(msg_url, msg, zh_msg["image_url"])


if __name__ == "__main__":

    # Start Settings
    printer_name = "MyPrinter"
    bark_api_iphone = "https://api.day.app/yourkey"
    obico_url = "http://example.com:3334"
    obico_token = "Your obico authentication token"
    # End Settings

    event_api_url = f"{obico_url}/api/v1/printer_events/?limit=1&filter_by_classes[]=ERROR&filter_by_classes[]=WARNING&filter_by_classes[]=SUCCESS&filter_by_classes[]=INFO&filter_by_types[]=ALERT&filter_by_types[]=ENDED&filter_by_types[]=STARTED&filter_by_types[]=PAUSE_RESUME&filter_by_types[]=FILAMENT_CHANGE&filter_by_types[]=PRINTER_ERROR"
    msg_api_url = f"{bark_api_iphone}/{printer_name}/"
    check_event(msg_api_url, event_api_url)