import twitter.TwitterCaller;
import twitter4j.*;

public class TestTwitterSearch {
	public static void main(String[] args) throws Exception {
		TwitterCaller twitter = new TwitterCaller("creds");
		Query query = new Query("from:realDonaldTrump");
	    QueryResult result = twitter.search(query);
	    for (Status status : result.getTweets()) {
	        System.out.println("@" + status.getUser().getScreenName() + ":" + status.getText());
	    }
	}
}
