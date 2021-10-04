#!/usr/bin/env python
"""Simple example of publish/subscribe illustrating topics.
Publisher and subscriber can be started in any order, though if publisher
starts first, any messages sent before subscriber starts are lost.  More than
one subscriber can listen, and they can listen to  different topics.
Topic filtering is done simply on the start of the string, e.g. listening to
's' will catch 'sports...' and 'stocks'  while listening to 'w' is enough to
catch 'weather'.
"""

# -----------------------------------------------------------------------------
#  Copyright (c) 2010 Brian Granger
#
#  Distributed under the terms of the New BSD License.  The full license is in
#  the file COPYING.BSD, distributed as part of this software.
# -----------------------------------------------------------------------------

import sys
import time
import json
import zmq


def main():
    if len(sys.argv) != 2:
        print('usage: publisher <bind-to>')
        sys.exit(1)

    bind_to = sys.argv[1]

    ctx = zmq.Context()
    s = ctx.socket(zmq.PUB)
    s.bind(bind_to)

    print("Starting broadcast on topics:")
    print("Hit Ctrl-C to stop broadcasting.")
    print("Waiting so subscriber sockets can connect...")
    print("")
    time.sleep(1.0)

    msg_body = "Helo Test Topic"
    topic =  'test'
    data = {
        "First":"1",
        "Second":"2",
        "Third":"3"
    }
    message = json.dumps(data)
    print('   Topic: %s, msg:%s' % (topic, msg_body))
    s.send_string(topic, zmq.SNDMORE)
    s.send_json(message)

    print("Sent Message" + message)
        
    print("Waiting for message queues to flush...")
    time.sleep(0.5)
    print("Done.")


if __name__ == "__main__":
    main()