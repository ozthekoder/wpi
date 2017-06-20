{
  'targets': [
    {
      'target_name': 'wiringPi',
      'sources': [
        'src/wpi.cc'
      ],
      'include_dirs': [
        '<!(node -e \"require(\'nan\')\")',
        'wiringpi/wiringPi',
        'wiringpi/devLib'
      ],
      'libraries': [
        '<!(pwd)/wiringpi/wiringPi/libwiringPi.a',
        '<!(pwd)/wiringpi/devLib/libwiringPiDev.a'
      ],
      'cflags': [
        '-Wall'
      ]
    }
  ]
}
