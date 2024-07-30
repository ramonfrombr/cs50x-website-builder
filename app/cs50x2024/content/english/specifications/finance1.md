<div class="alert alert-warning" data-alert="warning" role="alert"><p>If you used <code class="language-plaintext highlighter-rouge">wget</code> to download <code class="language-plaintext highlighter-rouge">finance.zip</code> before <a data-local="2024-04-10T08:30:00-04:00" href="https://time.cs50.io/20240410T083000-0400">2024-04-10T08:30:00-04:00</a>, be sure to copy, paste, and run this command <em>inside of your <code class="language-plaintext highlighter-rouge">finance</code> directory</em> in order to download a newer version of <code class="language-plaintext highlighter-rouge">helpers.py</code>:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>[ -f helpers.py ] &amp;&amp; curl -O https://cdn.cs50.net/2024/x/psets/9/finance/helpers.py
</code></pre></div></div></div>

# C$50 Finance

Implement a website via which users can “buy” and “sell” stocks, à la the below.

![C$50 Finance](https://cs50.harvard.edu/x/2024/psets/9/finance/finance_2024.png)

## Background

If you’re not quite sure what it means to buy and sell stocks (i.e., shares of a company), head [here](https://www.investopedia.com/articles/basics/06/invest1000.asp) for a tutorial.

You’re about to implement C$50 Finance, a web app via which you can manage portfolios of stocks. Not only will this tool allow you to check real stocks’ actual prices and portfolios’ values, it will also let you buy (okay, “buy”) and sell (okay, “sell”) stocks by querying for stocks’ prices.

Indeed, there are tools (one is known as IEX) that let you download stock quotes via their API (application programming interface) using URLs like `https://api.iex.cloud/v1/data/core/quote/nflx?token=API_KEY`. Notice how Netflix’s symbol (NFLX) is embedded in this URL; that’s how IEX knows whose data to return. That link won’t actually return any data because IEX requires you to use an API key, but if it did, you’d see a response in JSON (JavaScript Object Notation) format like this:

    {
      "avgTotalVolume":6787785,
      "calculationPrice":"tops",
      "change":1.46,
      "changePercent":0.00336,
      "close":null,
      "closeSource":"official",
      "closeTime":null,
      "companyName":"Netflix Inc.",
      "currency":"USD",
      "delayedPrice":null,
      "delayedPriceTime":null,
      "extendedChange":null,
      "extendedChangePercent":null,
      "extendedPrice":null,
      "extendedPriceTime":null,
      "high":null,
      "highSource":"IEX real time price",
      "highTime":1699626600947,
      "iexAskPrice":460.87,
      "iexAskSize":123,
      "iexBidPrice":435,
      "iexBidSize":100,
      "iexClose":436.61,
      "iexCloseTime":1699626704609,
      "iexLastUpdated":1699626704609,
      "iexMarketPercent":0.00864679844447232,
      "iexOpen":437.37,
      "iexOpenTime":1699626600859,
      "iexRealtimePrice":436.61,
      "iexRealtimeSize":5,
      "iexVolume":965,
      "lastTradeTime":1699626704609,
      "latestPrice":436.61,
      "latestSource":"IEX real time price",
      "latestTime":"9:31:44 AM",
      "latestUpdate":1699626704609,
      "latestVolume":null,
      "low":null,
      "lowSource":"IEX real time price",
      "lowTime":1699626634509,
      "marketCap":192892118443,
      "oddLotDelayedPrice":null,
      "oddLotDelayedPriceTime":null,
      "open":null,
      "openTime":null,
      "openSource":"official",
      "peRatio":43.57,
      "previousClose":435.15,
      "previousVolume":2735507,
      "primaryExchange":"NASDAQ",
      "symbol":"NFLX",
      "volume":null,
      "week52High":485,
      "week52Low":271.56,
      "ytdChange":0.4790450244167119,
      "isUSMarketOpen":true
    }

Notice how, between the curly braces, there’s a comma-separated list of key-value pairs, with a colon separating each key from its value. We’re going to be doing something very similar, with Yahoo Finance.

Let’s turn our attention now to getting this problem’s distribution code!

## Getting Started

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

    $

Next execute

    wget https://cdn.cs50.net/2024/x/psets/9/finance.zip

in order to download a ZIP called `finance.zip` into your codespace.

Then execute

    unzip finance.zip

to create a folder called `finance`. You no longer need the ZIP file, so you can execute

    rm finance.zip

and respond with “y” followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

    cd finance

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

    finance/ $

Execute `ls` by itself, and you should see a few files and folders:

    app.py  finance.db  helpers.py  requirements.txt  static/  templates/

If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!

### Running

Start Flask’s built-in web server (within `finance/`):

    $ flask run

Visit the URL outputted by `flask` to see the distribution code in action. You won’t be able to log in or register, though, just yet!

Within `finance/`, run `sqlite3 finance.db` to open `finance.db` with `sqlite3`. If you run `.schema` in the SQLite prompt, notice how `finance.db` comes with a table called `users`. Take a look at its structure (i.e., schema). Notice how, by default, new users will receive $10,000 in cash. But if you run `SELECT * FROM users;`, there aren’t (yet!) any users (i.e., rows) therein to browse.

Another way to view `finance.db` is with a program called phpLiteAdmin. Click on `finance.db` in your codespace’s file browser, then click the link shown underneath the text “Please visit the following link to authorize GitHub Preview”. You should see information about the database itself, as well as a table, `users`, just like you saw in the `sqlite3` prompt with `.schema`.
