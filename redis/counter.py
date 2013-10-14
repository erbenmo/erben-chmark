import redis
import datetime

def main():
    r = redis.StrictRedis(host='ec2-54-200-153-226.us-west-2.compute.amazonaws.com')
    r.set('foo', 'bar')
    print r.get('foo')

def test_counter():
    r = redis.StrictRedis(host='erben-chmark.1rfvi9.0001.usw2.cache.amazonaws.com')
    #r = redis.StrictRedis(host='ec2-54-200-153-226.us-west-2.compute.amazonaws.com')
    r.set('key', 1)

    print datetime.datetime.now()

    print r.get('key')
    for i in range(0, 500):
        r.incr('key', 1)
    print r.get('key')
        
    print datetime.datetime.now()
        

if __name__ == "__main__":
    test_counter()
