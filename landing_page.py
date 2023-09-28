import streamlit as st
from st_pages import Page, show_pages, add_page_title


show_pages(
  Section(name='Link Building Tools')
  Page("landing_page.py", "welcome"),
  Page("pages/1_Link_Checker.py", "Link Checker")
  Page("pages/15_Web_Explorer_Query_Generator.py", "Web Explorer Query Generator")
  Page("pages/16_Prospecting_Keyword_Analyzer.py", "Prospecting Keyword Analyzer")
  Page("pages/18_Prospecting_Cleanup_Tool.py", "Prospecting Cleanup Tool")
  Page("pages/17_Content_Refresh_Tools.py", "Content Refresh Tools")
  Page("pages/19_Pitchbox_Tag_Suggestor.py", "Pitchbox Tag Suggestor")
  Page("pages/10_Backlink_Relevance_Checker.py", "Backlink Relevance Checker")
  Section(name='SEO Tools')
  Page("pages/12_Keyword_Cannibalization_tool.py","Keyword Cannibalization tool")
  Page("pages/09_Algorithmic_Optimization_Tool.py","Algorithmic Optimization Tool")
  Page("pages/13_Title_Tag_Checker.py","Title Tag Checker")
  Page("pages/04_Internal_Linking_Tool.py","Internal Linking Tool")
  Page("pages/02_Bulk_URL_Removal_Tool.py","Bulk URL Removal Tool")
  Page("pages/02_Bulk_URL_Submission_Tool.py","Bulk URL Submission Tool")
  Page("pages/05_Google_Autocomplete_Scraper.py","Google Autocomplete Scraper")
  Page("pages/06_Question_Clustering_Tool.py","Question Clustering Tool")
  Page("pages/08_Relevant_Page_Finder.py","Relevant Page Finder")
)

st.title('''180 Marketing Tools



''')

st.header('''Link Building Tools



''')

st.markdown('''
[Link Checker]() - Checks a batch of domains to see if they pass 180’s quality guidelines.


[Web Explorer Query Generator](https://180marketing.streamlit.app/Web_Explorer_Query_Generator) - Paste in competitor domains to create custom prospecting queries for Ahrefs Web Explorer.


[Prospecting Keyword Analyzer](https://180marketing.streamlit.app/Prospecting_Keyword_Analyzer) - Find prospecting keywords for your client by uploading competitor backlinks from Ahrefs Web Explorer.


[Prospecting Cleanup Tool](https://180marketing.streamlit.app/Prospecting_Cleanup_Tool) - 
Upload a CSV file from Ahrefs Content Explorer or Ahrefs Web Explorer and the tool removes duplicate domains, dead websites, and prospects on spammy TLDs.


[Content Explorer Personalizer (Content Refresh)](https://180marketing.streamlit.app/Content_Refresh_Tools) - Provides personalized sentences you can use in your Content Refresh outreach emails.


[Subheading Suggestor (Content Refresh)](https://180marketing.streamlit.app/Content_Refresh_Tools) - Suggests additional subheadings that can be added to your Content Refresh outreach emails.


[Pitchbox Tag Suggestor](https://180marketing.streamlit.app/Pitchbox_Tag_Suggestor) - Get suggestions on the best tags to use for any domain.


[Backlink Relevance Checker](https://180marketing.streamlit.app/Backlink_Relevance_Checker) - Checks how relevant a batch of backlinks are to the client’s website.
''')

st.header('''SEO Tools



''')

st.markdown('''
[Keyword Cannibalization tool](https://180marketing.streamlit.app/Keyword_Cannibalization_tool) - Analyzes the client’s Queries report in Google Search Console to identify keyword cannibalization issues where multiple URLs are ranking for the same keywords. 


[Algorithmic Optimization Tool](https://180marketing.streamlit.app/Algorithmic_Optimization_Tool) - Uses AI to automatically generate title tags and meta description for the top pages on the client’s website.


[Title Tag Checker](https://180marketing.streamlit.app/Title_Tag_Checker) - Identifies the best keyword for the top pages on the client’s website, and checks to see if the keyword exists in the page’s title tag.


[Internal Linking Tool](https://180marketing.streamlit.app/Internal_Linking_Tool) - Paste in the blog post content as well as the website’s ranking data to quickly find internal linking opportunities.


[Bulk URL Removal Tool](https://180marketing.streamlit.app/Bulk_URL_Removal_Tool) - Paste in a batch of URLs to be removed from Google’s index using the IndexNow API.


[Bulk URL Submission Tool](https://180marketing.streamlit.app/Bulk_URL_Submission_Tool) - Paste in a batch of URLs to be removed from Google’s index using the IndexNow API.


[Google Autocomplete Scraper](https://180marketing.streamlit.app/Google_Autocomplete_Scraper) - Scrapes Google Autocomplete for relevant questions for up to 3 keywords. Very helpful for identifying subheadings for a blog post, or even blog post topics in general.


[Question Clustering Tool](https://180marketing.streamlit.app/Question_Clustering_Tool) - Clusters 100’s or even 1,000’s of questions into different groups by analyzing the words within each keyword phrase. Great for identifying the main questions on a topic, especially while building a Topical Map.


[Relevant Page Finder](https://180marketing.streamlit.app/Relevant_Page_Finder) - Input the client’s domain and up to 100 keywords to find the most relevant URL on the client’s website for each keyword.


''')





