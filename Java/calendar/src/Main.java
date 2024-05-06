import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    private static final Scanner scanner = new Scanner(System.in);

    static int getNumberFromUser(String text, int max) {
        System.out.println(text);
        int userChoice = scanner.nextInt();
        if (userChoice <= max) {
            return userChoice;
        }

        System.out.printf("You choice should be in smaller or equal to %d", max);
        return getNumberFromUser(text, max);
    }

    static int getNumberFromUser(String text, int max, int min) {
        System.out.println(text);
        int userChoice = scanner.nextInt();
        if (userChoice <= max && userChoice >= min) {
            return userChoice;
        }

        System.out.printf("You choice should be in range <%d, %d>", min, max);
        return getNumberFromUser(text, max, min);
    }

    static String getLineFromUser(String text) {
        System.out.println(text);
        return new Scanner(System.in).nextLine();
    }

    static void displayMainMenu() {
        System.out.println("""
        1. Add a new meeting
        2. Delete a meeting
        3. Show all meetings for a selected day
        4. Show all meetings for a selected day with selected priority
        5. Show all meetings for a selected day that start after chosen time
        6. Exit
        """);
    }

    static String getPriorityFromUser() {
        return switch(getNumberFromUser("Choose priority\n1. NORMAL\n2. HIGH\n3. EXTRA", 3)) {
            case 2 -> "HIGH";
            case 3 -> "EXTRA";
            default -> "NORMAL";
        };
    }

    static int getDayFromUser() {
        return getNumberFromUser("Choose day\n1. Monday\n2. Tuesday\n3. Wednesday\n4. Thursday\n5. Friday\n6. Saturday\n7. Sunday", 7);
    }


    static void addMeetingHandler(Calendar calendar) {
        int day = getDayFromUser();
        int startHour = getNumberFromUser("What is the starting hour of the meet", 23, Meet.earliestPossibleHour.getHour());
        int startMinute = getNumberFromUser("What is the starting minute of the meet", 59);
        int endHour = getNumberFromUser("What is the ending hour of the meet", 23, Meet.earliestPossibleHour.getHour());
        int endMinute = getNumberFromUser("What is the ending minute of the meet", 59);
        String priority = getPriorityFromUser();
        String description = getLineFromUser("Enter meet description");

        calendar.addMeet(description, day, startHour, startMinute, endHour, endMinute, priority);
    }

    static void removeMeetingHandler(Calendar calendar) {
        int day = getDayFromUser();

        if (calendar.getMeetingsForDay(day).isEmpty()) {
            System.out.println("There a no meeting this day");
            return;
        }

        int index = getNumberFromUser("Input number of the meeting you want to remove", calendar.getMeetingsForDay(day).size());
        calendar.removeMeet(day, index);
    }

    static void getMeetingsForDayHandler(Calendar calendar) {
        int day = getDayFromUser();
        ArrayList<Meet> meets = calendar.getMeetingsForDay(day);

        int index = 1;
        for (Meet meet: meets) {
            System.out.printf("<--- Meet %d --->\n", index);
            System.out.println(meet);
            index++;
        }
    }

    static void getMeetingsForDayWithPrioHandler(Calendar calendar) {
        int day = getDayFromUser();
        String priority = getPriorityFromUser();

        ArrayList<Meet> meets = calendar.getMeetingsForDayWithPriority(day, priority);

        for (Meet meet: meets) {
            System.out.println("<--- Meet--->");
            System.out.println(meet);
        }
    }

    static void getMeetingsForDayWithMinTimeHandler(Calendar calendar) {
        int day = getDayFromUser();
        int startingHour = getNumberFromUser("Choose min hour", 23, Meet.earliestPossibleHour.getHour());
        int startingMinute = getNumberFromUser("Choose min minute", 59);

        ArrayList<Meet> meets = calendar.getMeetingsForDayWithStartingHour(day, startingHour, startingMinute);

        for (Meet meet: meets) {
            System.out.println("<--- Meet--->");
            System.out.println(meet);
        }
    }

    static void addExample(Calendar calendar) {
        calendar.addMeet("one", 2, 8, 0, 8, 30, "NORMAL");
        calendar.addMeet("two", 2, 8, 30, 9, 0, "NORMAL");
        calendar.addMeet("three", 2, 9, 0, 9, 30, "EXTRA");
        calendar.addMeet("four", 2, 9, 30, 10, 0, "NORMAL");
        calendar.addMeet("five", 2, 10, 0, 10, 30, "EXTRA");
        calendar.addMeet("six", 2, 10, 30, 11, 0, "NORMAL");
        calendar.addMeet("seven", 2, 11, 0, 11, 30, "NORMAL");
    }



    public static void main(String[] args) {
        System.out.println("This program is meant to create a meetings calendar for the upcoming week :)");
        Calendar calendar = new Calendar();
        addExample(calendar);

        boolean userWantToContinue = true;
        while (userWantToContinue) {
            displayMainMenu();

            switch (getNumberFromUser("What do you want to do?", 6)) {
                case 1 -> addMeetingHandler(calendar);
                case 2 -> removeMeetingHandler(calendar);
                case 3 -> getMeetingsForDayHandler(calendar);
                case 4 -> getMeetingsForDayWithPrioHandler(calendar);
                case 5 -> getMeetingsForDayWithMinTimeHandler(calendar);
                case 6 -> userWantToContinue = false;
            }
        }

    }
}