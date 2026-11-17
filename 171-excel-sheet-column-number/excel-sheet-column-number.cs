public class Solution {
    public int TitleToNumber(string columnTitle) {
        long ans = 0;
        for (int i = 0; i < columnTitle.Length; i++) {
            char ch = columnTitle[i];
            ans = ans * 26 + (ch - 'A' + 1);
        }

        return (int) ans;
    }
}