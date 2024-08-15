import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class ListSetmap {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("Apple");
        list.add("Banana");

        Set<String> set = new HashSet<>();
        set.add("Red");
        set.add("Blue");

        Map<String, Integer> map = new HashMap<>();
        map.put("One", 1);
        map.put("Two", 2);

        // Printing the contents to verify
        System.out.println("List: " + list);
        System.out.println("Set: " + set);
        System.out.println("Map: " + map);
    }
}

