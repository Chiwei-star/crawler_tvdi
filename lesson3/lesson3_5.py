import json
from pprint import pprint

import argparse
import sys

class Site:
    def __init__(self, sitename, county, aqi, pollutant, status, pm2_5, pm2_5_avg, latitude, longitude, datacreationdate):
        self.sitename = sitename
        self.county = county
        self.aqi = aqi
        self.pollutant = pollutant
        self.status = status
        self.pm2_5 = pm2_5
        self.pm2_5_avg = pm2_5_avg
        self.latitude = latitude
        self.longitude = longitude
        self.datacreationdate = datacreationdate

def parse_sites_from_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    site_list = []
    for sitename in data['records']:
        site = Site(
            sitename=sitename['sitename'],
            county=sitename['county'],
            aqi=sitename['aqi'],
            pollutant=sitename['pollutant'],
            status=sitename['status'],
            pm2_5=sitename['pm2.5'],
            pm2_5_avg=sitename['pm2.5_avg'],
            latitude=sitename['latitude'],
            longitude=sitename['longitude'],
            datacreationdate=sitename['datacreationdate']
        )
        site_list.append(site)
    return site_list

def print_sites(sites):
    for s1 in sites:
        print("站點名稱:", s1.sitename)
        print("所在縣市:", s1.county)
        print("空氣品質指標 (AQI):", s1.aqi)
        print("主要污染物:", s1.pollutant)
        print("狀態:", s1.status)
        print("PM2.5 濃度:", s1.pm2_5)
        print("PM2.5 平均濃度:", s1.pm2_5_avg)
        print("緯度:", s1.latitude)
        print("經度:", s1.longitude)
        print("資料建立日期:", s1.datacreationdate)
        print("=================")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="查詢空氣品質資料")
    parser.add_argument('--county', type=str, help='指定縣市名稱')
    parser.add_argument('--file', type=str, default='aqx_p_488.json', help='資料檔案名稱')
    args = parser.parse_args()

    sites = parse_sites_from_json(args.file)
    if args.county:
        filtered = [s for s in sites if s.county == args.county]
        if not filtered:
            print(f"找不到縣市: {args.county}")
            sys.exit(1)
        print_sites(filtered)
    else:
        print_sites(sites)