
#include <SPI.h>
#include <RadioLib.h>

// ===== CC1101 PINS =====
#define CC_CS 10
#define CC_GDO0 3
#define CC_GDO2 4

// ===== RF SETTINGS =====
const float RF_FREQ = 434.0;   // MHz
const int8_t RF_POWER = -10;  // dBm, requested output level

// Keep disabled until RF setup and authorization are verified.
const bool ENABLE_RF_TX = false;

// ===== CC1101 =====
CC1101 radio = new Module(
  CC_CS,
  CC_GDO0,
  RADIOLIB_NC,
  CC_GDO2
);

void setup() {
  Serial.begin(115200);

  // Wait briefly for the Serial Monitor to connect.
  unsigned long startTime = millis();

  while (!Serial && millis() - startTime < 5000) {
    delay(10);
  }

  delay(1000);

  Serial.println("Arduino serial connection established!");

  SPI.begin();

  Serial.println("Initializing CC1101...");

  // Initialize the radio at the chosen RF frequency.
  int state = radio.begin(
    RF_FREQ,
    10.0,    // Bitrate (unused for unmodulated carrier)
    40.0,    // Frequency deviation
    464.0,   // Receiver bandwidth
    RF_POWER
  );

  if (state != RADIOLIB_ERR_NONE) {
    Serial.print("Initialization failed: ");
    Serial.println(state);
    return;
  }

  Serial.println("CC1101 initialized!");

  if (!ENABLE_RF_TX) {
    Serial.println("RF transmission disabled.");
    return;
  }

  // Start continuous unmodulated carrier transmission.
  state = radio.transmitDirect();

  if (state == RADIOLIB_ERR_NONE) {
    Serial.println("Continuous RF carrier active!");
    Serial.print("Frequency: ");
    Serial.print(RF_FREQ);
    Serial.println(" MHz");
  } else {
    Serial.print("TX failed: ");
    Serial.println(state);
  }
}

void loop() {
  // No packet transmission needed.
}
