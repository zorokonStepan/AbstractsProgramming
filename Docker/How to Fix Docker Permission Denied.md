https://phoenixnap.com/kb/docker-permission-denied

```
    sudo groupadd -f docker       - Enter the command below to create the docker group on the system.
    sudo usermod -aG docker $USER - Type the following usermod command to add the active user to the docker group.
    newgrp docker                 - Apply the group changes to the current terminal session by typing
    groups                        - Check if the docker group is in the list of user groups
```