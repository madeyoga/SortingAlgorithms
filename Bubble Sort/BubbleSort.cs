public static void BubbleSort(this List<int> item)
{
    int temp;
    for (var i = 0; i < item.Count; i++)
    {
        for (var j = i; j < item.Count; j++)
        {
            if (item[i] > (item[j]))
            {
                temp = item[j];
                item[j] = item[i];
                item[i] = temp;
            }
        }
    }
}
