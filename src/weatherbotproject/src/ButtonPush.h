#ifndef BUTTONPUSH_H
#define BUTTONPUSH_H

#include <ros.h>

struct ButtonPushRequest {
  uint32_t push;
};

struct ButtonPushResponse {
  bool check;
};

#endif  // MY_SERVICE_H

