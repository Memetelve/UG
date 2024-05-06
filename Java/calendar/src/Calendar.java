import java.time.LocalTime;
import java.util.ArrayList;

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

    public ArrayList<Meet> getMeetingsForDay(int day) {
        return meetings.get(day - 1);
    }

    public ArrayList<Meet> getMeetingsForDayWithPriority(int day, String priority) {

        ArrayList<Meet> resultMeetings = new ArrayList<Meet>();

        for (Meet meet : meetings.get(day - 1)) {
            if (meet.getPriority().equals(priority)) {
                resultMeetings.add(meet);
            }
        }

        return resultMeetings;
    }

    public ArrayList<Meet> getMeetingsForDayWithStartingHour(int day, int minHour, int minMinute) {
        ArrayList<Meet> resultMeetings = new ArrayList<Meet>();

        LocalTime minTime = LocalTime.of(minHour, minMinute);

        for (Meet meet : meetings.get(day - 1)) {
            if (meet.getStartTime().isAfter(minTime) || meet.getStartTime().equals(minTime) ) {
                resultMeetings.add(meet);
            }
        }

        return resultMeetings;
    }
}
