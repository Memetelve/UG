import java.time.LocalTime;



public class Meet {
    public static final LocalTime earliestPossibleHour = LocalTime.of(8, 0);
    private final String description;
    private final LocalTime startTime;
    private final LocalTime endTime;
    private final String priority;

    public Meet(String description, LocalTime startTime, LocalTime endTime, String priority) {
        this.description = description;
        this.startTime = startTime;
        this.endTime = endTime;
        this.priority = priority;
    }

    public String getPriority() {
        return priority;
    }

    public LocalTime getStartTime() {
        return startTime;
    }

    @Override
    public String toString() {
        return String.format("%s - %s\nPriority: %s\nDescription: %s\n", startTime, endTime, priority, description);
    }
}
