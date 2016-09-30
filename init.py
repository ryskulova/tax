#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from urllib import pathname2url as quote

name = 'Рыскулова'

cookies = {
    'ASP.NET_SessionId': 'uhuymc55w0e35xjrc11jvx55',
    'Lng': '1049',
    '_ga': 'GA1.2.1836223811.1473689884',
}

headers = {
    'Origin': 'https://e-taxservices.kg',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8,ru;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'X-MicrosoftAjax': 'Delta=true',
    'Referer': 'https://e-taxservices.kg/WorkWithTP/TPInfoByTIN.aspx?lang=ru',
}

data = 'ctl00%24scriptMgr=ctl00%24PageUpdatePanel%7Cctl00%24cphMain%24btnCheckByName&ctl00_scriptMgr_HiddenField=&__VIEWSTATE=&ctl00%24hdnSessionGuid=d3276cc7-2839-43bf-b29b-26123a002ab7&ctl00%24hdnShouldBeAccessedWithoutSession=1&ctl00%24hdnIsLeftMenuInitialized=&ctl00%24cphMain%24SearchMethods=rdoSearchMethodByName&ctl00%24cphMain%24txtTIN=&ctl00%24cphMain%24txtName='+quote(name)+'&ctl00%24hidLastTabClicked=-1&ctl00%24hidLastLayerNum=&__EVENTTARGET=&__EVENTARGUMENT=&__VSTATE=eNrlV3tvG1kVTyZ%2B5FkDSyO0IOcW2nWMxuNX3qlXbNNlFWiz0Tb0nyjyXs%2Fc2JOOZ9K54yRms1If7C6oKxAFBELqLpWQEH%2BA0jRp3EdciU9wLfEJEJ%2BAL7Ccc2em7ooW%2BAP%2BAUce33vOueec33nNzWe9ia%2F0RpPl8oJje65j8XfY1YbpsmWHe%2BeofuW7rFkuj%2FZFv657Vi53Wt%2BsXaSmfdo1nEuMunrtIvNqjnGuubK49G%2FJfONfyCzROktEB%2FO5qZnc5GxxcioxOpwcWKZVtmgbbCfam0sO4%2B4C5d7K8uJ5JIwg4dum26UMbwJl2WVbSCj8LdbT29PT8xl88Bc%2FEVz8WbnU5B6rawuOZTHdMx2ba28xm7mmrl0wufdufnX1n4hAbC5Tq8GWqem%2BW3gmumh7xYJK6lx3XMusqOQyczkcLBW0HP6pZKFheQ2XlWzW8FxqqWS5UbFMHfStOFeYXapMT9NJfXIqP1ucYLmZ2TX1v6h77T%2Bsrg8iGyub4C2Plrn5fdZf3vK1Auevvf%2F78Vxd6%2B8fUHq6n7jchKXX95f%2FgxgMJRNc9rVpVy95LjyjXxV%2FFI%2FFgdjr%2FFAcin0ifte5JY7FfXgeJU%2Ba%2FCLdedbm7zCq15hRHVXWE8ZoTFHgGVH6Eydjr2UXnHrdsbPfoVuU66656WU3rjaY28zktRktr9VNW9vg%2BZeLNUwpWShqeoN7Tj048bUXnKjDkGEuMF99AROixYA19gLWesMO0rrBz7zUE013LMetODsgZSgDidFIMrLCdrzoH%2FrO%2BoKvjwwSMh5qGzdVrjpqVXVVqtbT75mrqbccp2qxN2xqNT1T529XNqCeUmsld95cdddK%2BNjdfXY%2B%2FZ7Uh1Ttasn%2F2d1dXUtrmw1eG6dutVFntsfT76uSaZXy37TZNjlPPTaenqclrukug82bFkPBcSetosY6MKrMC6gcBj2t4hwH%2FmpubZ5qlDdtvZSHFXf1UnW%2Brm1SF0SXHINpps2Z651j6xDPcQSGKt9Pj2%2BbtuFsq4ajS6%2FUlB%2BTlJrKZre3t7WqxJ6hIXgIZz3b3W1wkKzSVHp%2BZBA1Vul4yvc%2BpZLU997ITEwVC7np6clMHgks49EdcGTL1BnXrlTlOf8UZ7aBIvhO2TLZdqDybDZIUjJ%2B2eRmxWJVQ4kkRpWxWLTdK24TsR%2FU%2BhMi7nWuweamOBKHsDokot25IR6Jx50fdz7q%2FFQck251qEQ8FW3xQOwB%2B6Z42LkOonuoLZAXLSAcPneCiBZ0VguUBnZu%2BCJw8mMiHpHOddijFnAFOq4tnnRuElB%2FANsWECQzONjuXOvcPGUoMei4L68nAE4yvuI41oq5aRiG0uvjs8RthAGKftKF%2BRANoVEwh96ENsFt0daIuAurNmBroQnAhSDA%2BqF0%2BwN4HsC5JzAOgAxjAljHuNEMaH9p9YS4A%2BQH6DUeNpS%2BhM8YhLge%2BHiNZzk4D6TH6N9TP%2BaBiT20uUdCyBL%2Bh3489n384MURQPoQURhKNLBx2igWpqd0fTpTmCnOZiaKlfVMpTBbyRSm8oUizeUKtDIN1vshcHJqKWGwXhG%2FBOX3JeojiMGepgGmIRD5EiAAkXgtFI7XfIORsZiRjL9pU6gqowZa476qmvgZeHgdFOEcvSYDvA8RPEZMiBUDBNEW9%2BG775PuyjJ6IO4h9F93bgFAOXMhTZiPh0T8BkMnnoLUPawjILdwHuHIDbwaHez6J12OGehosIj7HsOEvwu5OZQhvYGl9xSdBBuPOx%2FjUVTqSw5C%2FdzyE%2BIz%2BoKAhfm8jZ5hHRsYKUkk4ldQED%2BQGXri58fPbhs5d8QdQ5HlGqm5bD1azEpxmWUA9ug5cXQHEuEHCAsUqkSDMbPTTdmw%2BBTbBGz9CEpK%2BaL0qx8b4BV%2FGT0jfiGVI0rZCgdgxV89wFrEIECJGsrJ4MDJ7oE2tEsLYg2lAALDYcFEAvzxKr7yMMzJAdOGa0HNq0MZYLwjY0Ng%2Befd5pANJCtaPPTNdm6drbjZ11GLXzVDrBve8Inp%2FIIPdVRCbWE1fC6YhsxKIPTqPwi1wkxLQSyFZJR7TYtFRwyTb1q0OWc7NpsHJL2hoduyVg%2BC%2BeXbIX4Xx5L9C5wvWJTzqEJIcgBuAxeYXfVqyolkpHzq0jlFARODb9tw6YCLPYidcRlcSmxi8qVGvcJcYIyzLXxTEK9mcm0Lr1HpbgMPdjGEDTUcPRE6W7Ec%2Fcpz3r4mfgsOfkKyfk%2BFcGXR%2BLlFxqe%2B95GxEfR6LKEoxssMDmCIhsqnFuHKteA0bE%2FB%2F0cShjIC%2BegPzX4LWqg7q%2F1Z9VxDy3aFVwe8BA5B5lgOA%2BgSskv%2B9PtCLl%2FUwqGIRRSW8%2Bd8%2BgTkj6B09oN2ROoSO890i7oUrwlkC%2B99k9okgWSwesVqEgPemnOgfiqTm8nkJkh%2BZi4%2FMZeb0ArTJA%2FSsxoySSE3V8zPFScN4%2B%2FNlYlO&__ASYNCPOST=true&ctl00%24cphMain%24btnCheckByName=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA'

temp = requests.post('https://e-taxservices.kg/WorkWithTP/TPInfoByTIN.aspx?lang=ru', headers=headers, cookies=cookies, data=data)

print temp.text
