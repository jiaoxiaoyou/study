#!/usr/bin/env bash

ADDRESS=$1

if [ -z $ADDRESS ]; then
  ADDRESS="localhost:9200"
fi

# Check that Elasticsearch is running
curl -s "http://$ADDRESS" 2>&1 > /dev/null
if [ $? != 0 ]; then
    echo "Unable to contact Elasticsearch at $ADDRESS"
    echo "Please ensure Elasticsearch is running and can be reached at http://$ADDRESS/"
    exit -1
fi

echo "WARNING, this script will delete the 'good' and the 'myindex' indices and re-index all data!"
echo "Press Control-C to cancel this operation."
echo
echo "Press [Enter] to continue."
read

# Delete the old index, swallow failures if it doesn't exist
curl -s -XDELETE "$ADDRESS/goods" > /dev/null

# creat goods
curl -s -XPUT "$ADDRESS/goods" > /dev/null

# Create the next index using mapping.json
#echo "Creating 'goods' index..."
#curl -s -XPUT -H'Content-Type: application/json' "$ADDRESS/goods" -d@$(dirname $0)/mapping.json

# Wait for index to become yellow
curl -s "$ADDRESS/goods/_health?wait_for_status=yellow&timeout=10s" > /dev/null
echo
echo "Done creating 'goods' index."

echo "creat mapping"
curl -s -XPOST "$ADDRESS/goods/_mapping" -H'Content-Type: application/json' -d'{
	"_source" : {
      "enabled" : true
    },
	"properties": {
    "created_on": {
      "type": "date",
      "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd"
    }
  }
}'

echo
echo "Indexing data..."

echo "Indexing groups..."
curl -s -XPOST "$ADDRESS/goods/_doc/1" -H'Content-Type: application/json' -d'{
	"name": "xiangjiao",
    "price": 60,
    "producer": "zhongguo",
    "desc": "xiangtian,kekou",
	"created_on": "2019-04-25 10:00:00",
    "tags": [
        "chang",
        "zhi",
        "huang"
    ]
}'

echo
curl -s -XPOST "$ADDRESS/goods/_doc/2" -H'Content-Type: application/json' -d'{
    "name": "pingguo",
    "price": 20,
    "producer": "zhongguo",
    "desc": "haixing,haochi",
	"created_on": "2020-01-25 10:00:00",
    "tags": [
        "da",
        "yuan"
    ]
}'

echo
curl -s -XPOST "$ADDRESS/goods/_doc/3" -H'Content-Type: application/json' -d'{
	"name": "lzi",
    "price": 10,
    "producer": "zhongguo",
    "desc": "zide",
	"created_on": "2020-04-01 10:00:00",
    "tags": [
        "suan",
        "tian"
    ]
}'

echo
curl -s -XPOST "$ADDRESS/goods/_doc/4" -H'Content-Type: application/json' -d'{
    "name": "boluo",
    "price": 74,
    "producer": "zhongguo",
    "desc": "getouda",
	"created_on": "2020-04-11 10:00:00",
    "tags": [
        "huang",
        "youci"
    ]
}'

echo
curl -s -XPOST "$ADDRESS/goods/_doc/5" -H'Content-Type: application/json' -d'{
    "name": "mihoutao",
    "price": 45,
    "producer": "xinxilan",
    "desc": "suan",
	"created_on": "2020-04-21 10:00:00",
    "tags": [
        "lv",
        "huang"
    ]
}'

echo
curl -s -XPOST "$ADDRESS/goods/_doc/6" -H'Content-Type: application/json' -d'{
    "name": "xigua",
    "price": 109,
    "producer": "zhongguo",
    "desc": "haochi",
	"created_on": "2020-04-25 10:00:00",
    "tags": [
        "da",
        "haochi"
    ]
}'

echo
curl -s -XPOST "$ADDRESS/goods/_doc/7" -H'Content-Type: application/json' -d'{
    "name": "pingguo",
    "price": 109,
    "producer": "zhongguo",
    "desc": "haochi",
	"created_on": "2020-04-26 10:00:00",
    "tags": [
        "da",
        "haochi"
    ]
}'

echo
curl -s -XPOST "$ADDRESS/goods/_doc/8" -H'Content-Type: application/json' -d'{
    "name": "pingguo",
    "price": 109,
    "producer": "zhongguo",
    "desc": "haochi",
	"created_on": "2020-04-27 10:00:00",
    "tags": [
        "da",
        "haochi"
    ]
}'

echo
curl -s -XPOST "$ADDRESS/goods/_doc/9" -H'Content-Type: application/json' -d'{
    "name": "pingguo",
	"price": 120,
	"producer": "USA",
	"desc": "haochi",
	"created_on": "2020-04-28 10:00:00",
	"tags": [
	"da",
	"haochi"
	]
}'

echo
curl -s -XPOST "$ADDRESS/goods/_doc/10" -H'Content-Type: application/json' -d'{
    "name": "pingguo",
	"price": 220,
	"producer": "USA",
	"desc": "haochi",
	"created_on": "2020-04-29 10:00:00",
	"tags": [
	"da",
	"haochi"
	]
}'

echo
echo "Done indexing groups."


echo
