int maxProfit(int* prices, int pricesSize) {
    if (pricesSize < 2) {
        return 0; 
    }

    int minPrice = prices[0]; 
    int maxProfit = 0; 

    for (int i = 1; i < pricesSize; i++) {
        int profit = prices[i] - minPrice;
        if (profit > maxProfit) {
            maxProfit = profit;
        }
        if (prices[i] < minPrice) {
            minPrice = prices[i];
        }
    }

    return maxProfit;
}
