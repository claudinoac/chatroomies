workspace "Chatroomies" "C4 architecture model." {

    model {
        user = Person "User" "Active user in the chatroom."
        chatroomies = softwareSystem "Chatroomies application." "Chatroomies application" {
            chatroomiesDB = container "Database" "Chatroomies DB"
            chatroomiesWeb = container "Chatroomies Web" "Web Server"
            chatroomiesBotReceiver = container "Chatroomies bot receiver" "Receives chatroomiesBot command results."
        }
        chatroomiesBot = softwareSystem "Chatroomies bot system" "Chatroomies bot system."
        broker = softwareSystem "Broker" "Communication gateway"
        user -> chatroomiesWeb "Uses" "Websockets"
        chatroomiesWeb -> broker "Send command" "Event"
        broker -> chatroomiesBot "Send command" "Event"
        chatroomiesBot -> broker "Send command result" "Event"
        broker -> chatroomiesBotReceiver "Send command result" "Event"
        chatroomiesBotReceiver -> chatroomiesDB "Send command result" "Message"

        chatroomiesWeb -> chatroomiesBot "Send command" "Event"
        chatroomiesBot -> chatroomiesBotReceiver "Send command result" "Event"
        chatroomiesWeb -> chatroomiesDB "Uses"

    }

    views {
        systemLandscape chatroomies "SystemOverview" "Chatroomies System" {
            include *
            exclude chatroomies -> chatroomiesBot
            exclude chatroomiesBot -> chatroomies
        }
        container chatroomies "ApplicationPerspective" {
            include *
            exclude broker
        }
        styles {
            element "Software System" {
                background #1168bd
                color #ffffff
            }
            element "container"  {
                background #000000
                color #ffffff
            }
            element "Person" {
                shape person
                background #08427b
                color #ffffff
            }
        }
    }
    
}
