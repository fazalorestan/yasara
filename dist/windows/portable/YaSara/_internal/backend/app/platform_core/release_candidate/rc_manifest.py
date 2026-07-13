class InternalRCManifest:
    def manifest(self):
        return {
            'ready': True,
            'build_id': '2026.50.E.001',
            'channel': 'internal-rc',
            'target': 'windows',
            'manual_auto_trading_toggle': True,
            'signal_only_default': True,
            'auto_trading_default': False,
            'final_exe_generated': False
        }
internal_rc_manifest = InternalRCManifest()
