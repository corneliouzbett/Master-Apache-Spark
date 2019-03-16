from pyspark import SparkContext, SparkConf

def display_words(words):
    for w, we in words.items():
        print("{} : {}".format(w, we))

if __name__ == "__main__":
    conf = SparkConf().setAppName("word count").setMaster("local[2]")
    sc = SparkContext(conf = conf)

    lines = sc.textFile("in/word_count.text")

    total_lengths = lines.map(lambda s: len(s)).reduce(lambda a,b: a+b)

    words = lines.flatMap(lambda line: line.split(" "))

    wordCounts = words.countByValue()

    display_words(wordCounts)
