#!/usr/bin/node
function callMeMoby (x, func) {
  for (let i = 0; i < x; i++) {
    func(); // why not a return?
  }
}

module.exports.callMeMoby = callMeMoby;
