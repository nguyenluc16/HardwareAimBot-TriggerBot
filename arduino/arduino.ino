#ifdef dobogusinclude
#include <spi4teensy3.h>
#endif
#include <SPI.h>

#include "hidcustom.h"

signed char delta[3] = {0, 0, 0};

void MouseRptParser::Parse(USBHID *hid, bool is_rpt_id, uint8_t len, uint8_t *buf)
{
  MYMOUSEINFO *pmi = (MYMOUSEINFO *)buf;

  if (CHECK_BIT(prevState.mouseInfo.buttons, MOUSE_LEFT) != CHECK_BIT(pmi->buttons, MOUSE_LEFT))
  {
    if (CHECK_BIT(pmi->buttons, MOUSE_LEFT))
      Mouse.press(MOUSE_LEFT);
    else
      Mouse.release(MOUSE_LEFT);
  }

  if (CHECK_BIT(prevState.mouseInfo.buttons, MOUSE_RIGHT) != CHECK_BIT(pmi->buttons, MOUSE_RIGHT))
  {
    if (CHECK_BIT(pmi->buttons, MOUSE_RIGHT))
      Mouse.press(MOUSE_RIGHT);
    else
      Mouse.release(MOUSE_RIGHT);
  }

  if (CHECK_BIT(prevState.mouseInfo.buttons, MOUSE_MIDDLE) != CHECK_BIT(pmi->buttons, MOUSE_MIDDLE))
  {
    if (CHECK_BIT(pmi->buttons, MOUSE_MIDDLE))
      Mouse.press(MOUSE_MIDDLE);
    else
      Mouse.release(MOUSE_MIDDLE);
  }

  if (CHECK_BIT(prevState.mouseInfo.buttons, MOUSE_PREV) != CHECK_BIT(pmi->buttons, MOUSE_PREV))
  {
    if (CHECK_BIT(pmi->buttons, MOUSE_PREV))
      Mouse.press(MOUSE_PREV);
    else
      Mouse.release(MOUSE_PREV);
  }

  if (CHECK_BIT(prevState.mouseInfo.buttons, MOUSE_NEXT) != CHECK_BIT(pmi->buttons, MOUSE_NEXT))
  {
    if (CHECK_BIT(pmi->buttons, MOUSE_NEXT))
      Mouse.press(MOUSE_NEXT);
    else
      Mouse.release(MOUSE_NEXT);
  }

  if (pmi->dX || pmi->dY)
    OnMouseMove(pmi);

  if (pmi->wheel)
    OnWheelMove(pmi);

  prevState.bInfo[0] = buf[0];
}

void MouseRptParser::OnMouseMove(MYMOUSEINFO *mi)
{
  delta[0] = mi->dX;
  delta[1] = mi->dY;
}

void MouseRptParser::OnWheelMove(MYMOUSEINFO *mi)
{
  delta[2] = mi->wheel;
}

#include <usbhub.h>

USB Usb;
USBHub Hub(&Usb);
HIDBoot<USB_HID_PROTOCOL_MOUSE> HidMouse(&Usb);

MouseRptParser Prs;

void setup()
{
  Serial.begin(115200);
  Serial.setTimeout(1);
  Usb.Init();
  HidMouse.SetReportParser(0, &Prs);
  Mouse.begin();
}

/*Delay simulates user behavior*/
/*
void humanMove(signed char dx, signed char dy, signed char wheel) {
  if (dx == 0 && dy == 0 && wheel == 0) return;

  int steps = max(max(abs(dx), abs(dy)), abs(wheel));
  float stepX = (float)dx / steps;
  float stepY = (float)dy / steps;
  float stepW = (float)wheel / steps;

  for (int i = 0; i < steps; ++i) {
    signed char jitterX = random(-1, 2);  // ±1
    signed char jitterY = random(-1, 2);
    signed char jitterW = random(-1, 2);

    Mouse.move((signed char)(stepX + jitterX),
               (signed char)(stepY + jitterY),
               (signed char)(stepW + jitterW));

    delay(random(2, 5));  // delay mô phỏng hành vi người dùng
  }
}

void loop()
{
  delta[0] = 0;
  delta[1] = 0;
  delta[2] = 0;

  Usb.Task();

  if (Serial.available() > 0)
  {
    char inChar = Serial.read();
    if (inChar == 'M') {
      Serial.readBytes((char *)&delta, 3);  // Đọc đủ 3 byte
      humanMove(delta[0], delta[1], delta[2]);
    }
    else if (inChar == 'C') {
      Mouse.click();
    }
  }
}

*/

void loop()
{
  delta[0] = 0;
  delta[1] = 0;
  delta[2] = 0;
  Usb.Task();

  if (Serial.available() > 0)
  {
    char inChar = Serial.read();
    if (inChar == 'M')
      Serial.readBytes((char *)&delta, 2);
    else if (inChar == 'C')
      Mouse.click();
  }
  Mouse.move(delta[0], delta[1], delta[2]);
}