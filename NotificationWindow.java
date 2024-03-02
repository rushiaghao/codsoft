import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class NotificationWindow extends JFrame {
    private JLabel titleLabel;
    private JLabel messageLabel;
    private JLabel imageLabel;
    private JButton closeButton;

    public NotificationWindow() {
        super("Notification");
        initializeComponents();
        setupLayout();
        setSize(300, 150);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    private void initializeComponents() {
        titleLabel = new JLabel("Title");
        messageLabel = new JLabel("Message");
        imageLabel = new JLabel(new ImageIcon("icon.png")); // Provide path to your icon/image
        closeButton = new JButton("Close");
        closeButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dispose();
            }
        });
    }

    private void setupLayout() {
        JPanel panel = new JPanel(new BorderLayout());
        JPanel contentPanel = new JPanel(new BorderLayout());
        JPanel buttonPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));

        contentPanel.add(titleLabel, BorderLayout.NORTH);
        contentPanel.add(messageLabel, BorderLayout.CENTER);
        contentPanel.add(imageLabel, BorderLayout.WEST);

        buttonPanel.add(closeButton);

        panel.add(contentPanel, BorderLayout.CENTER);
        panel.add(buttonPanel, BorderLayout.SOUTH);

        add(panel);
    }

    public void setTitle(String title) {
        titleLabel.setText(title);
    }

    public void setMessage(String message) {
        messageLabel.setText(message);
    }

    public void setImageIcon(Icon icon) {
        imageLabel.setIcon(icon);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                NotificationWindow notificationWindow = new NotificationWindow();
                notificationWindow.setTitle("New Notification");
                notificationWindow.setMessage("You have a new notification!");
                notificationWindow.setImageIcon(new ImageIcon("icon.png")); // Provide path to your icon/image
                notificationWindow.setVisible(true);
            }
        });
    }
}
