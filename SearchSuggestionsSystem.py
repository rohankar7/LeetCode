# 1268. Search Suggestions System
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        productList = []
        string = ""
        for w in searchWord:
            string += w
            temp = []
            for prod in products:
                if string == prod[:len(string)] and len(temp)<3: temp.append(prod)
            productList.append(temp)
        return productList