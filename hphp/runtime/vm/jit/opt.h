/*
   +----------------------------------------------------------------------+
   | HipHop for PHP                                                       |
   +----------------------------------------------------------------------+
   | Copyright (c) 2010-present Facebook, Inc. (http://www.facebook.com)  |
   +----------------------------------------------------------------------+
   | This source file is subject to version 3.01 of the PHP license,      |
   | that is bundled with this package in the file LICENSE, and is        |
   | available through the world-wide-web at the following url:           |
   | http://www.php.net/license/3_01.txt                                  |
   | If you did not receive a copy of the PHP license and are unable to   |
   | obtain it through the world-wide-web, please send a note to          |
   | license@php.net so we can mail you a copy immediately.               |
   +----------------------------------------------------------------------+
*/
#pragma once

#include "hphp/runtime/vm/jit/id-set.h"
#include "hphp/runtime/vm/jit/ssa-tmp.h"
#include "hphp/runtime/vm/jit/types.h"

namespace HPHP::jit {

//////////////////////////////////////////////////////////////////////

struct IRUnit;

//////////////////////////////////////////////////////////////////////

/*
 * The main optimization passes.
 */
void optimizeRefcounts(IRUnit&);
void selectiveWeakenDecRefs(IRUnit&);
void optimizePredictions(IRUnit&);
bool gvn(IRUnit&);
void optimizeLoads(IRUnit&);
void optimizeStores(IRUnit&);
void optimizeVanillaChecks(IRUnit&);
void cleanCfg(IRUnit&);
bool optimizePhis(IRUnit&);
bool optimizeCheckTypes(IRUnit&);
void sinkDefs(IRUnit&);

/*
 * For debugging, we can run this pass, which inserts various sanity checking
 * assertion instructions.
 */
void insertAsserts(IRUnit&);

/*
 * Run all the optimization passes.
 */
void optimize(IRUnit& unit, TransKind kind);

//////////////////////////////////////////////////////////////////////

}
