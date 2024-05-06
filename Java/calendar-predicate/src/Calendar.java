import java.time.LocalTime;
import java.util.ArrayList;
import java.util.function.Predicate;

public class Calendar {
    private final ArrayList<ArrayList<Meet>> meetings = new ArrayList<ArrayList<Meet>>();

    public Calendar() {
        for (int i = 0; i < 7; i++) {
            meetings.add(new ArrayList<>());
        }
    }

    public void addMeet(String description, int day, int startHour, int startMinute, int endHour, int endMinute, String priority) {

        LocalTime startTime = LocalTime.of(startHour, startMinute);
        LocalTime endTime = LocalTime.of(endHour, endMinute);

        meetings.get(day - 1).add(new Meet(description, startTime, endTime, priority));
    }

    public void removeMeet(int day, int index) {
        meetings.get(day - 1).remove(index - 1);
    }

    public ArrayList<Meet> getMeetingsForDay(int day, Predicate<Meet> condition) {
        ArrayList<Meet> resultMeetings = new ArrayList<>();

        for (Meet meet : meetings.get(day - 1)) {
            if (condition.test(meet)) {
                resultMeetings.add(meet);
            }
        }

        return resultMeetings;
    }
}
