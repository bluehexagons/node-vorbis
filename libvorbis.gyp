# This file is used with the GYP meta build system.
# http://code.google.com/p/gyp
# To build try this:
#   svn co http://gyp.googlecode.com/svn/trunk gyp
#   ./gyp/gyp -f make --depth=. libvorbis.gyp
#   make
#   ./out/Debug/test

{
  'variables': {
    'target_arch%': 'ia32', # build for a 32-bit CPU by default
    'ogg_include_dirs%': [],
    'ogg_libraries%': [ '-logg' ],
  },
  'target_defaults': {
    'default_configuration': 'Debug',
    'configurations': {
      'Debug': {
        'defines': [ 'DEBUG', '_DEBUG' ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 1, # static debug
          },
        },
      },
      'Release': {
        'defines': [ 'NDEBUG' ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 0, # static release
          },
        },
      }
    },
    'msvs_settings': {
      'VCLinkerTool': {
        'GenerateDebugInformation': 'true',
      },
    },

    # common vorbis stuff
    'include_dirs': [
      # platform and arch-specific headers
      'config/<(OS)/<(target_arch)',
      # the location of the libogg header files
      '<@(ogg_include_dirs)',
      'libvorbis/include',
      'libvorbis/lib',
      'libvorbis',
    ],
    'direct_dependent_settings': {
      'include_dirs': [
        # platform and arch-specific headers
        'config/<(OS)/<(target_arch)',
        # the location of the libogg header files
        '<@(ogg_include_dirs)',
        'libvorbis/include',
      ],
    },
    'link_settings': {
      'libraries': [
        '<@(ogg_libraries)',
      ]
    },
    'conditions': [
      ['OS=="mac"', {
        'defines': [
          'DARWIN',
          'USE_MEMORY_H',
        ],
        'conditions': [
          ['target_arch=="ia32"', { 'xcode_settings': { 'ARCHS': [ 'i386' ] } }],
          ['target_arch=="x64"', { 'xcode_settings': { 'ARCHS': [ 'x86_64' ] } }]
        ],
      }],
      ['OS!="win"', {
        'defines': [
          'PIC',
          'HAVE_CONFIG_H',
        ],
      }]
    ],
  },

  'targets': [

    # libvorbisenc
    {
      'target_name': 'vorbisenc',
      'product_prefix': 'lib',
      'type': 'static_library',
      'dependencies': [ 'libvorbis' ],
      'sources': [
        'libvorbis/lib/vorbisenc.c'
      ]
    },

    # libvorbisfile
    {
      'target_name': 'vorbisfile',
      'product_prefix': 'lib',
      'type': 'static_library',
      'dependencies': [ 'libvorbis' ],
      'sources': [
        'libvorbis/lib/vorbisfile.c'
      ]
    },

    # libvorbis
    {
      'target_name': 'libvorbis',
      'product_prefix': '',
      'type': 'static_library',
      'sources': [
        'libvorbis/lib/mdct.c',
        'libvorbis/lib/smallft.c',
        'libvorbis/lib/block.c',
        'libvorbis/lib/envelope.c',
        'libvorbis/lib/window.c',
        'libvorbis/lib/lsp.c',
        'libvorbis/lib/lpc.c',
        'libvorbis/lib/analysis.c',
        'libvorbis/lib/synthesis.c',
        'libvorbis/lib/psy.c',
        'libvorbis/lib/info.c',
        'libvorbis/lib/floor1.c',
        'libvorbis/lib/floor0.c',
        'libvorbis/lib/res0.c',
        'libvorbis/lib/mapping0.c',
        'libvorbis/lib/registry.c',
        'libvorbis/lib/codebook.c',
        'libvorbis/lib/sharedbook.c',
        'libvorbis/lib/lookup.c',
        'libvorbis/lib/bitrate.c',
      ],
    },

    {
      'target_name': 'test',
      'type': 'executable',
      'dependencies': [ 'libvorbis' ],
      'sources': [ 'libvorbis/examples/decoder_example.c' ]
    },
  ]
}
