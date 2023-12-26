# hoymiles_proto

This library helps with talking to and simulating Hoymiles microinverters.

It uses *asyncio* and has various helper classes. While many things are obviously unfinished,
I hope the general approach is rather stable. My intention is to publish this on PyPi some day.

## Preparations

Execute:
1. Extract the `protoc` executable from a recent [protobuf](https://github.com/protocolbuffers/protobuf/releases) release into the main directory. Version 25.0 works fine.
   ```bash
   wget https://github.com/protocolbuffers/protobuf/releases/download/v25.1/protoc-25.1-linux-x86_64.zip
   unzip protoc-25.1-linux-x86_64.zip
   ```

2. Install dependent packages via your system package manager or `pip install`:
    * `asyncio`
    * `crcmod`
    * `datetime`
    * `enum`
    * `importlib`
    * `protobuf`
    * `random`
    * `struct`
    * `time`
   ```bash
   sudo pip install asyncio crcmod datetime importlib protobuf
   #sudo pip install enum random struct time
   ```
   
3. Execute `./gen_protos.py`

   ```bash
   vi gen_protos.py
   # Execute protoc (preferring executable in current directory).
   os.environ['PATH'] = './bin/:' + os.environ['PATH']
   ./gen_protos.py
   ```

4. Execute `./gen_message_classes.py`

   ```bash
   ./gen_message_classes.py
   ```

## Random notes
* At least the integrated DTU of HMS-800W-2T allows only a single connection at a time. Opening another connection to its port 10081 will close the existing one (usually - I think I had one situation where the new connection was closed). So expect to be disconnected at any time. You might also receive a response for a command that was triggered on the old connection. This isn't handled well by the library currently.

* I have renamed many messages and fields from Hoymiles' original protobuf files for clarity. Especially, there were many cases like this: Their Cloud sends `CommandRes` and receives a `CommandReq` from the DTU. Usually, we would expect that the **req**uest is sent first and is answered with a **res**ponse, right? It seems that in their code, `...Req` simply means "coming from the DTU" and `...Res` means "sent to the DTU". I have renamed these messages to `...FromDtu` and `...ToDtu` to make it more clear. `gen_message_classes.py` contains information about the direction per message type and creates aliases like `Cloud.Command.Req` which point to the appropriate message (`CommandToDtu` in this case).

* I intended to let `Connection` handle auto-reconnect, but I'm no longer sure whether that would be a good idea. A connection has some amount of state information and in enough cases there message belong together as a group/transaction. For example, requesting realtime date requires an `ACTION_POLL_ALL` to be sent before, and `Command` + `CommandStatus` belong together. So it's probably better to let the user of the library handle that.

* I guess the `wnum` field in the realtime data could be used to detect that there are new alarms, and only fetch them if the number has changed.

* `mi_signal` seems to be constantly increasing in two (hex) positions, then going back to 0. Not sure about the purpose.
