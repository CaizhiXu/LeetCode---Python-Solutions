## https://leetcode.com/problems/accounts-merge/

from collections import defaultdict


class Solution1:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_acc = defaultdict(list)
        for i, acc in enumerate(accounts):
            for j in range(1, len(acc)):
                email_acc[acc[j]].append(i)

        def dfs(i, emails):
            if i in visited:
                return
            visited.add(i)
            acc = accounts[i]
            for email in acc[1:]:
                emails.add(email)
                for id in email_acc[email]:
                    dfs(id, emails)

        res = []
        visited = set()
        for i, acc in enumerate(accounts):
            if i not in visited:
                name = acc[0]
                emails = set()
                dfs(i, emails)
                res.append([name] + sorted(emails))
        return res


from collections import defaultdict


class Solution2:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]
        email_acc = {}

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email not in email_acc:
                    email_acc[email] = i
                else:
                    parent[find(i)] = find(email_acc[email])
        print(parent)

        res = []
        acc_email = defaultdict(list)
        for i, acc in enumerate(accounts):
            acc_email[find(i)].extend(acc[1:])

        for acc in acc_email:
            name = accounts[acc][0]
            res.append([name] + sorted(set(acc_email[acc])))

        return res

