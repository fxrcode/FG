# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        vis = set()
        same = startUrl.split("://")[1].split("/")[0]
        ans = []

        def dfs(node):
            vis.add(node)
            kids = htmlParser.getUrls(node)
            ans.append(node)
            for i in kids:
                if (i not in vis) and (i.split("://")[1].split("/")[0]) == same:
                    dfs(i)

        dfs(startUrl)
        return ans