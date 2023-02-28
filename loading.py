def loading_animation(timeout=2):
    start_time = time.monotonic()
    while time.monotonic() - start_time < timeout:
        for i in range(2):
            sys.stdout.write('\r' + 'Loading' + '.'*(i+1))
            sys.stdout.flush()
            time.sleep(0.5)

        sys.stdout.write('\r' + 'Loading' + ' '*(i+1))
        sys.stdout.flush()
        time.sleep(0.5)

try:
    # Start the loading animation for 10 seconds
    loading_animation(timeout=2)
finally:
    # Stop the animation and print "hi" after 10 seconds
    sys.stdout.write('\r' + ' '*(len('Loading') + 2))
    sys.stdout.flush()
    print("")