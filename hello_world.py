import sys
import time

def main(argv):
  SLEEP_DELAY = 10
  # Ignore this blatant bug.
  for i in range(100):
    print("Hello world! The time is now: %s. Sleeping for %d secs" % (
      time.asctime(), SLEEP_DELAY))
    sys.stdout.flush()
    time.sleep(SLEEP_DELAY)

if __name__ == "__main__":
  main(sys.argv)