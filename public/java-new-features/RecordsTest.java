import java.util.List;
import java.util.stream.Collectors;

public class RecordsTest {

    public static void main(String[] args) {
        System.out.println("Shri Ganesh");
        record Person (String name, int age){}
        Person p1= new Person("a", 20);
        Person p2= new Person("b", 20);

        String s = "abc";
        List<String> list = s.lines().collect(Collectors.toList());
        list.forEach(System.out::println);

        System.out.println("Main ends.");
    }


}
