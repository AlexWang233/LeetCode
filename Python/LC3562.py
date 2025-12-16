class Solution:
    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int,
    ) -> int:
        graph = defaultdict(lambda: [])
        for u, v in hierarchy:
            graph[u - 1].append(v - 1)

        @lru_cache
        def dfs(emp_id: int, discounted: bool):
            purchase_price = present[emp_id]
            if discounted:
                purchase_price //= 2
            bought_profit = defaultdict(lambda: -999999)
            if purchase_price <= budget:
                bought_profit[purchase_price] = future[emp_id] - purchase_price
            nb_profit = defaultdict(lambda: -999999)
            nb_profit[0] = 0

            for child in graph[emp_id]:
                discounted_child = dfs(child, True)
                nd_child = dfs(child, False)

                new_bought = defaultdict(lambda: -999999)
                for cost, profit in bought_profit.items():
                    for c2, p2 in discounted_child.items():
                        total_profit = profit + p2
                        total_cost = cost + c2
                        if total_cost <= budget:
                            new_bought[total_cost] = max(
                                new_bought[total_cost], total_profit
                            )
                bought_profit = new_bought

                new_nb = defaultdict(lambda: -999999)
                for cost, profit in nb_profit.items():
                    for c2, p2 in nd_child.items():
                        total_profit = profit + p2
                        total_cost = cost + c2
                        if total_cost <= budget:
                            new_nb[total_cost] = max(new_nb[total_cost], total_profit)
                nb_profit = new_nb

            res = nb_profit.copy()
            for cost, profit in bought_profit.items():
                res[cost] = max(res[cost], profit)
            # print(emp_id, res)
            return res

        ans = dfs(0, False)
        return max(ans.values()) if len(ans) > 0 else 0
