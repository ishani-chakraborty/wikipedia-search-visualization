## What is data visualization?

Data visualization is the graphic representation of data. It involves producing images that communicate relationships among the represented data to viewers of the images. This communication is achieved through the use of a systematic mapping between graphic marks and data values in the creation of the visualization.

## What is a wordcloud?

An image composed of words used in a particular text or subject, in which the size of each word indicates its frequency or importance.

## Installation

Install [wordcloud](https://github.com/amueller/word_cloud) using a simple pip command.

```
pip install wordcloud
```

**wikipedia** library is used for extracting wikipedia articles on any given topic. Install it using this pip command:
```
pip install wikipedia
```
## Usage

Run python script as:

```
python mywiki.py <query>
```

For example:

```
python mywiki.py code
```

will create wordcloud for the topic 'code' which looks like this:

![](https://raw.githubusercontent.com/ishani-chakraborty/wikipedia-search-visualization/master/result.png)
