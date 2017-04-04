package twitter;
import java.io.File;
import java.io.IOException;
import org.apache.commons.io.FileUtils;
import com.google.gson.Gson;
import twitter4j.*;
import twitter4j.auth.AccessToken;

public class TwitterCaller {
	private TwitterCreds creds;
	private Twitter twitter;
	
	public TwitterCaller(String credsPath) throws IOException{
		creds = loadCreds(credsPath);
		twitter = TwitterFactory.getSingleton();
		twitter.setOAuthConsumer(creds.consumer_key, creds.consumer_secret);
		twitter.setOAuthAccessToken(new AccessToken(creds.access_token, creds.access_token_secret));
	}
	public TwitterCreds loadCreds(String filePath) throws IOException{
		String json = FileUtils.readFileToString(new File(filePath));
		return new Gson().fromJson(json, TwitterCreds.class);
	}
	public QueryResult search(Query q) throws TwitterException{
		return twitter.search(q);
	}
	
	public class TwitterCreds {
		private String consumer_key;
		private String consumer_secret;
		private String access_token;
		private String access_token_secret;
		
		public String getConsumer_key() {
			return consumer_key;
		}
		public void setConsumer_key(String consumer_key) {
			this.consumer_key = consumer_key;
		}
		public String getConsumer_secret() {
			return consumer_secret;
		}
		public void setConsumer_secret(String consumer_secret) {
			this.consumer_secret = consumer_secret;
		}
		public String getAccess_token() {
			return access_token;
		}
		public void setAccess_token(String access_token) {
			this.access_token = access_token;
		}
		public String getAccess_token_secret() {
			return access_token_secret;
		}
		public void setAccess_token_secret(String access_token_secret) {
			this.access_token_secret = access_token_secret;
		}
	}
}
