{
  'targets': [
    {
      'target_name': 'vorbis',
      'include_dirs': [ "<!(node -e \"require('nan')\")" ],
      'sources': [
        'src/binding.cc',
      ],
      'dependencies': [
        'libvorbis.gyp:libvorbis',
        'libvorbis.gyp:vorbisenc',
      ],
    }
  ]
}
